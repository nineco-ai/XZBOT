import re
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

@st.cache_data
def get_coordinates(address):
    """주소를 위도/경도로 변환하는 함수 - '대한민국' 접두어 추가"""
    if not address:  # 주소가 빈 문자열이면 None 반환
        return None
    try:
        geolocator = Nominatim(user_agent="my_streamlit_app")
        query = "대한민국 " + address
        location = geolocator.geocode(query)
        if location:
            return (location.latitude, location.longitude)
        return None
    except GeocoderTimedOut:
        time.sleep(1)
        return get_coordinates(address)
    except Exception as e:
        print(f"Error: {e}")
        return None

def extract_dong(addr):
    """주소에서 행정동(예: '미산동', '은행동') 추출 (정규표현식은 상황에 따라 수정 필요)"""
    m = re.search(r'시흥시\s+(\S+동)', addr)
    if m:
        return m.group(1)
    return None

def main():
    st.title('시흥XZ 청년단 회사 위치 지도')
    
    # 데이터 하드코딩 (예시)
    data = {
        '회사명': [
            '㈜쿨원', '㈜이아이', '㈜옹옹', '우수기공', '㈜뉴에이지원', 
            '대종테크', '특허법인 키', '㈜나인코', '선수정밀', '에스비에이치이', 
            '체이드', '태광특수고무', '토탈솔루션', '대유콤푸레샤', 
            '㈜ 포유 (FOUR U)', 'FT SOLUTIONS(에프티솔루션스)', 
            '성현정밀', '㈜ 지제이테크', 'T.M.C', '에바다푸드시스템', 
            '하성엔프라', '지엠씨', '㈜이니티움', '나비', 
            '㈜한울컴퍼니', '코파츠', '비더원(BE THE ONE)', 
            '㈜ 메코텍티타늄', '배우미', '제이어스가죽공방', 
            'SM박스', '선우특수소재', '㈜ 엑사솔루션', 
            '스마트세무법인', '해봄인테리어', '㈜툴스미스', 
            '㈜리더스알앤디', '이수테크놀로지', '한스', '엠텍코리아'
        ],
        '주소': [
            '경기도 시흥시 미산동 140-16',
            '경기도 시흥시 은행동 247-1',
            '경기도 시흥시 대야동 657-2',
            '경기도 시흥시 미산동 234-37',
            '경기도 시흥시 신천동 864-4',
            '경기도 시흥시 안현동 360-7',
            '경기도 시흥시 정왕동 1800-3',
            '경기도 시흥시 광석동 134-2',
            '경기도 시흥시 포동 20-71',
            '경기도 시흥시 정왕동 1800-3',
            '경기도 시흥시 정왕동 2087-5',
            '경기도 시흥시 신천동 864-4',
            '경기도 시흥시 신천동 864-4',
            '경기도 시흥시 과림동 63-1',
            '경기도 시흥시 정왕동 1284-13',
            '경기도 시흥시 미산동 234-12',
            '경기도 시흥시 정왕동 1255-10',
            '경기도 시흥시 정왕동 1289-8',
            '경기도 시흥시 안현동 446-12',
            '경기도 시흥시 월곶동 1011-24',
            '경기도 시흥시 미산동 234-12',  # 예시: 하성엔프라 주소
            '경기도 시흥시 배곧동 204',
            '경기도 시흥시 정왕동 1800-3',
            '경기도 시흥시 정왕동 1800-3',
            '경기도 시흥시 신천동 158-3',
            '경기도 시흥시 정왕동 1800-3',
            '경기도 시흥시 정왕동 1800-3',
            '경기도 시흥시 정왕동 1274-5',
            '경기도 시흥시 정왕동 1731-18',
            '경기도 시흥시 신천동 752',
            '경기도 시흥시 미산동 562-1',
            '경기도 시흥시 신천동 864-4',
            '경기도 시흥시 정왕동 1800-3',
            '경기도 시흥시 정왕동 1610',
            '경기도 시흥시 은행동 529-4',
            '경기도 시흥시 대야동 660',
            '경기도 시흥시 정왕동 1800-3',
            '경기도 시흥시 정왕동 1255-10',
            '경기도 시흥시 정왕동 1277-14',
            '경기도 시흥시 정왕동 1288-2'
        ]
    }
    
    df = pd.DataFrame(data)
    
    st.subheader("회원 정보")
    st.dataframe(df)
    
    # 먼저 좌표 변환 시도 결과를 저장 (좌표, dong 등)
    coords_list = []
    dong_map = {}
    failed_indices = []
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for idx, row in df.iterrows():
        progress_bar.progress((idx + 1) / len(df))
        status_text.text(f"처리 중... {idx + 1}/{len(df)}")
        
        coord = get_coordinates(row['주소'])
        dong = extract_dong(row['주소'])
        coords_list.append(coord)
        
        if coord:
            # 동별로 좌표 저장
            if dong:
                dong_map.setdefault(dong, []).append(coord)
        else:
            failed_indices.append(idx)
    
    progress_bar.empty()
    status_text.empty()
    
    # 실패한 주소들에 대해, 같은 동에서 좌표가 있는 경우 평균 좌표로 대체
    for idx in failed_indices:
        addr = df.loc[idx, '주소']
        dong = extract_dong(addr)
        if dong and dong in dong_map and len(dong_map[dong]) > 0:
            # 평균 좌표 계산
            lat = sum([pt[0] for pt in dong_map[dong]]) / len(dong_map[dong])
            lon = sum([pt[1] for pt in dong_map[dong]]) / len(dong_map[dong])
            coords_list[idx] = (lat, lon)
    
    # 좌표 결과를 df에 추가
    df['coords'] = coords_list
    
    st.subheader("회사 위치 지도")
    m = folium.Map(location=[37.3799, 126.8031], zoom_start=12)
    
    # 개별 마커를 지도에 추가
    for idx, row in df.iterrows():
        if row['coords']:
            folium.Marker(
                location=row['coords'],
                popup=f"회사명: {row['회사명']}<br>주소: {row['주소']}",
                tooltip=row['회사명']
            ).add_to(m)
    
    folium_static(m)
    
    st.subheader("통계")
    st.write(f"총 회사 수: {len(df)}")
    failed_companies = [df.loc[idx, '회사명'] for idx in failed_indices if not coords_list[idx]]
    if failed_companies:
        st.warning("다음 회사의 주소를 찾지 못했습니다: " + ", ".join(failed_companies))
    
    st.subheader("지역별 분포")
    area_counts = df['주소'].str.extract(r'시흥시\s+(\S+)')[0].value_counts()
    st.bar_chart(area_counts)

if __name__ == "__main__":
    main()

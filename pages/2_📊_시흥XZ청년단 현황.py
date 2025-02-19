import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

# 캐시된 좌표 변환 함수
@st.cache_data
def get_coordinates(address):
    """주소를 위도/경도로 변환하는 함수 - '대한민국' 접두어 추가"""
    if not address:  # 주소가 빈 문자열이면 None 반환
        return None
    try:
        geolocator = Nominatim(user_agent="my_streamlit_app")
        # '대한민국'을 접두어로 추가하여 geocoding 정확도 향상
        query = "대한민국 " + address
        location = geolocator.geocode(query)
        if location:
            return location.latitude, location.longitude
        return None
    except GeocoderTimedOut:
        time.sleep(1)  # 요청 간에 1초 대기
        return get_coordinates(address)
    except Exception as e:
        print(f"Error: {e}")  # 오류 메시지 출력
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
            '경기도 시흥시 미산동 234-12',  # 하성엔프라의 주소가 누락되어 빈 문자열 처리
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
    
    st.subheader("회사 위치 지도")
    m = folium.Map(location=[37.3799, 126.8031], zoom_start=12)
    
    # MarkerCluster 추가: 겹치는 마커 그룹화
    marker_cluster = MarkerCluster().add_to(m)
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    failed_companies = []  # 좌표 변환 실패한 회사 기록
    
    for idx, row in df.iterrows():
        progress = (idx + 1) / len(df)
        progress_bar.progress(progress)
        status_text.text(f"처리 중... {idx + 1}/{len(df)}")
        
        coords = get_coordinates(row['주소'])
        if coords:
            folium.Marker(
                coords,
                popup=f"회사명: {row['회사명']}<br>주소: {row['주소']}",
                tooltip=row['회사명']
            ).add_to(marker_cluster)
        else:
            failed_companies.append(row['회사명'])
    
    progress_bar.empty()
    status_text.empty()
    
    folium_static(m)
    
    st.subheader("통계")
    st.write(f"총 회사 수: {len(df)}")
    if failed_companies:
        st.warning("다음 회사의 주소를 찾지 못했습니다: " + ", ".join(failed_companies))
    
    st.subheader("지역별 분포")
    area_counts = df['주소'].str.extract(r'시흥시\s+(\S+)')[0].value_counts()
    st.bar_chart(area_counts)

if __name__ == "__main__":
    main()

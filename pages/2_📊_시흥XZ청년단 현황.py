import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

# 캐시된 좌표 변환 함수
@st.cache_data
def get_coordinates(address):
    """주소를 위도/경도로 변환하는 함수"""
    try:
        geolocator = Nominatim(user_agent="my_streamlit_app")
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        return None
    except GeocoderTimedOut:
        time.sleep(1)
        return get_coordinates(address)

def main():
    st.title('시흥XZ 청년단 회사 위치 지도')
    
    # 실제 데이터를 여기에 하드코딩 (예시 데이터)
    # 실제 엑셀 파일의 데이터로 교체해야 합니다
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
                    '경기도 시흥시 미산로 18,18-1',
        '경기도 시흥시 은행로 42 서광테크노타운 102호',
        '경기도 시흥시 은계로 338번길 36, 3층 301호',
        '경기도 시흥시 양우재길 17-22',
        '경기도 시흥시 포도원로 116번길 25 프라임지식산업센터 411호',
        '경기도 시흥시 수인로 3087번길7',
        '경기도 시흥시 마유로 376, 시흥창업센터 207호',
        '경기도 시흥시 광석동 134-2',
        '경기도 시흥시 새우개2길 46(포동)',
        '경기도 시흥시 마유로 376, 시흥창업센터 415호',
        '경기도 시흥시 희망공원로 77, 3동 1층',
        '경기도 시흥시 신천동 864-4',
        '경기도 시흥시 포도원로 116번길 25 프라임지식산업센터 706호',
        '경기도 시흥시 금오로 607-22',
        '경기도 시흥시 소망공원로 306',
        '경기도 시흥시',
        '경기도 시흥시 옥구천동로218 타원타크라6차 B동 602호',
        '경기도 시흥시 공단1대로321번길 4',
        '경기도 시흥시 수인로 3000-82',
        '경기도 시흥시 월곶해안로 161번길 20',
        '경기도 시흥시 서울대학로 278번길 61 323-1',
        '경기도 시흥시 마유로 376, 시흥창업센터 407호',
        '경기도 시흥시 마유로 376, 201-48호',
        '경기도 시흥시 신천동 158-3',
        '경기도 시흥시 마유로 376, 413호',
        '경기도 시흥시 마유로 376, 410호',
        '경기도 시흥시 소망공원로 283',
        '경기도 시흥시 서촌상가 2길 25-1, 405호',
        '경기도 시흥시 신천2길 23. 2층',
        '경기도 시흥시 구수미1길 74-5 SM박스',
        '경기도 시흥시 포도원로 116번길 25, 212호',
        '경기도 시흥시 마유로 376 창업센터 501-4',
        '경기도 시흥시 정왕대로233번길 18, 3층',
        '경기 시흥시 대은로104번길 14 1층',
        '경기도 시흥시 은계중앙로 306번길 55 311호',
        '경기도 시흥시 마유로 376, 416호',
        '경기도 시흥시 옥구천동로218 타원타크라6차 B동 602호',
        '경기도 시흥시 경기과기대로 219 길산SST지식산업센터 6층 615호',
        '경기도 시흥시 정왕천로 197 동우 디지털단지 B동 216호',
        ]
    }
    print(data)  # data의 내용을 출력하여 확인
    
    max_length = max(len(v) for v in data.values())
    for key in data.keys():
        while len(data[key]) < max_length:
            data[key].append(None)  # None 또는 적절한 기본값으로 채움
    
    df = pd.DataFrame(data)
    
    # 데이터프레임 표시
    st.subheader("회원 정보")
    st.dataframe(df)
    
    # 지도 생성
    st.subheader("회사 위치 지도")
    m = folium.Map(location=[37.3799, 126.8031], zoom_start=12)
    
    # 진행 상황 표시
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # 각 주소에 대해 위도/경도 변환 및 마커 추가
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
            ).add_to(m)
    
    # 진행 상황 표시 제거
    progress_bar.empty()
    status_text.empty()
    
    # 지도 표시
    folium_static(m)
    
    # 데이터 통계
    st.subheader("통계")
    st.write(f"총 회사 수: {len(df)}")
    
    # 지역별 분포
    st.subheader("지역별 분포")
    area_counts = df['주소'].str.extract(r'시흥시\s+(\S+)')[0].value_counts()
    st.bar_chart(area_counts)

if __name__ == "__main__":
    main()

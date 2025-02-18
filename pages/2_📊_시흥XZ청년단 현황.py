import streamlit as st
import folium
from streamlit_folium import folium_static

# 예시 데이터
companies = [
    {"name": "회사 A", "location": [37.5012, 127.0396]},  # 서울 강남구
    {"name": "회사 B", "location": [35.1662, 129.1652]}  # 부산 해운대구
]

# 지도 생성
m = folium.Map(location=[36.3504, 127.3848], zoom_start=7)  # 대한민국 중앙 좌표

# 회사 마킹
for company in companies:
    folium.Marker(
        location=company['location'],
        popup=company['name'],
        tooltip=company['name']
    ).add_to(m)

# Streamlit에 지도 표시
folium_static(m)
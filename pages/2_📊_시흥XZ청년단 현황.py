import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

st.set_page_config(page_title="회사 위치 표시 서비스", page_icon="🏢")
st.markdown("# 회사 위치 표시 서비스")

# 구글 스프레드시트를 CSV로 불러오기 위한 URL 구성
# 원본 링크: 
# https://docs.google.com/spreadsheets/d/1FX49voSom_dLr_tMXUd95g-_yNoDxlg-kEriNHR0t0g/edit?gid=1606270629#gid=1606270629
# CSV 다운로드 링크:
sheet_url = (
    "https://docs.google.com/spreadsheets/d/1FX49voSom_dLr_tMXUd95g-_yNoDxlg-kEriNHR0t0g/"
    "export?format=csv&gid=1606270629"
)

st.write("구글 스프레드시트에서 데이터 불러오는 중...")
try:
    df = pd.read_csv(sheet_url)
except Exception as e:
    st.error("데이터 불러오기 실패: " + str(e))
    st.stop()

st.write("데이터 미리보기:")
st.dataframe(df.head())

# 스프레드시트에 회사명을 담은 '회사명' 컬럼과 주소를 담은 '주소' 컬럼이 있다고 가정합니다.
if "회사명" not in df.columns or "주소" not in df.columns:
    st.error("스프레드시트에 '회사명'과 '주소' 컬럼이 필요합니다.")
    st.stop()

st.write("주소를 좌표로 변환 중... (약간의 시간이 소요될 수 있습니다)")

# geopy의 Nominatim 사용 (무료 서비스라서 호출 제한에 유의)
geolocator = Nominatim(user_agent="myGeocoder")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

def get_lat_lon(address):
    location = geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# 각 주소를 지오코딩하여 위도/경도 컬럼 추가
df["lat"] = None
df["lon"] = None

for idx, row in df.iterrows():
    lat, lon = get_lat_lon(row["주소"])
    df.at[idx, "lat"] = lat
    df.at[idx, "lon"] = lon

st.write("좌표 변환 완료!")
st.dataframe(df.head())

# 위도/경도 정보가 없는 행은 제거
df = df.dropna(subset=["lat", "lon"])

# GeoDataFrame 생성
gdf = gpd.GeoDataFrame(
    df,
    geometry=[Point(x, y) for x, y in zip(df["lon"], df["lat"])],
    crs="EPSG:4326"
)

# 지도 그리기 (matplotlib 이용)
fig, ax = plt.subplots(figsize=(8, 8))

# 회사 위치 마커 표시 (빨간색 원)
gdf.plot(ax=ax, color="red", markersize=50, label="회사 위치")

# 각 마커 옆에 회사명 텍스트 추가
for idx, row in gdf.iterrows():
    ax.annotate(
        row["회사명"],
        (row["lon"], row["lat"]),
        xytext=(3, 3),
        textcoords="offset points",
        fontsize=9
    )

ax.set_title("회사 위치 지도")
ax.set_xlabel("경도")
ax.set_ylabel("위도")
ax.legend()

st.pyplot(fig)

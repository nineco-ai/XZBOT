import streamlit as st
import pandas as pd
import requests
import time
import re
import json
import streamlit.components.v1 as components

# 네이버 지오코딩 API를 사용한 좌표 변환 함수
@st.cache_data
def get_coordinates(address):
    """주소를 위도/경도로 변환 (네이버 지오코딩 API 사용)"""
    if not address:
        return None
    client_id = "4w2120h8i6"         # 네이버 클라우드 플랫폼에서 발급받은 Client ID
    client_secret = "M4K2SNk548aDUap1e3sgQrJ3P2uiIkz6abh8GS7A"   # 네이버 클라우드 플랫폼에서 발급받은 Client Secret
    # 대한민국 접두어 추가 (검색 정확도 향상)
    query = "대한민국 " + address
    url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={query}"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if result['addresses']:
                # 네이버 API는 'x'에 경도, 'y'에 위도를 반환
                lat = float(result['addresses'][0]['y'])
                lon = float(result['addresses'][0]['x'])
                return (lat, lon)
    except Exception as e:
        st.error(f"Geocoding error: {e}")
    return None

def extract_dong(addr):
    """
    주소에서 행정동 추출
    예: '경기도 시흥시 미산동 140-16' → '미산동'
    (정규표현식은 필요에 따라 수정)
    """
    m = re.search(r'시흥시\s+(\S+동)', addr)
    if m:
        return m.group(1)
    return None

def main():
    st.title("시흥XZ 청년단 회사 위치 (Naver 지도)")
    
    # 예시 데이터 (행정동 주소 형식)
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
            '경기도 시흥시 미산동 234-12',
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
    
    # 좌표 계산 및 동별 그룹화
    coords_list = []
    dong_map = {}
    failed_indices = []
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for idx, row in df.iterrows():
        progress_bar.progress((idx + 1) / len(df))
        status_text.text(f"Processing {idx + 1}/{len(df)}")
        coord = get_coordinates(row['주소'])
        dong = extract_dong(row['주소'])
        coords_list.append(coord)
        if coord:
            if dong:
                dong_map.setdefault(dong, []).append(coord)
        else:
            failed_indices.append(idx)
    
    progress_bar.empty()
    status_text.empty()
    
    # 실패한 주소는 같은 동의 평균 좌표로 대체
    for idx in failed_indices:
        addr = df.loc[idx, '주소']
        dong = extract_dong(addr)
        if dong and dong in dong_map and len(dong_map[dong]) > 0:
            avg_lat = sum(pt[0] for pt in dong_map[dong]) / len(dong_map[dong])
            avg_lon = sum(pt[1] for pt in dong_map[dong]) / len(dong_map[dong])
            coords_list[idx] = (avg_lat, avg_lon)
    
    df['coords'] = coords_list
    
    # 마커 데이터를 준비 (회사명, 주소, 위도, 경도)
    marker_data = []
    for idx, row in df.iterrows():
        if row['coords']:
            marker_data.append({
                'company': row['회사명'],
                'address': row['주소'],
                'lat': row['coords'][0],
                'lon': row['coords'][1]
            })
    marker_data_json = json.dumps(marker_data)
    
    # 네이버 지도 HTML 생성
    naver_client_id = "YOUR_NAVER_CLIENT_ID"  # 지도 표시용 Client ID
    html_string = f"""
    <html>
      <head>
        <meta charset="utf-8">
        <script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId={naver_client_id}"></script>
        <style>
          #map {{
            width: 100%;
            height: 650px;
          }}
        </style>
      </head>
      <body>
        <div id="map"></div>
        <script>
          var map = new naver.maps.Map('map', {{
            center: new naver.maps.LatLng(37.3799, 126.8031),
            zoom: 12
          }});
          var markerData = {marker_data_json};
          markerData.forEach(function(item) {{
            var marker = new naver.maps.Marker({{
              position: new naver.maps.LatLng(item.lat, item.lon),
              map: map,
              title: item.company + "\\n" + item.address
            }});
            var infoWindow = new naver.maps.InfoWindow({{
              content: '<div style="padding:5px;">회사명: ' + item.company + '<br>주소: ' + item.address + '</div>'
            }});
            naver.maps.Event.addListener(marker, "click", function(e) {{
              infoWindow.open(map, marker);
            }});
          }});
        </script>
      </body>
    </html>
    """
    
    st.subheader("회사 위치 지도 (Naver 지도)")
    components.html(html_string, height=700)
    
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

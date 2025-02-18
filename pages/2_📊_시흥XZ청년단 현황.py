import streamlit as st
import pandas as pd
import requests
from urllib.parse import urlparse, parse_qs
import json

def parse_naver_cafe_url(url):
    """네이버 카페 URL을 파싱하여 필요한 정보를 추출합니다."""
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')
    
    cafe_id = path_parts[0]  # xzceo
    article_id = path_parts[1]  # 42
    
    return {
        'cafe_id': cafe_id,
        'article_id': article_id
    }

def create_viewer_app():
    st.set_page_config(page_title="네이버 카페 게시글 뷰어", page_icon="📑")
    
    st.title("네이버 카페 게시글 뷰어")
    
    # URL 입력 필드
    cafe_url = st.text_input(
        "네이버 카페 URL을 입력하세요",
        value="https://cafe.naver.com/xzceo/42?art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtY2FmZS1wcg.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6Inh6Y2VvIiwiYXJ0aWNsZUlkIjo0MiwiaXNzdWVkQXQiOjE3Mzk4MzgxNjkyMDR9.fZfJOICqOZD1upcpqmwRxHH_oP4CfFeEaGee01Sgz4o"
    )
    
    if cafe_url:
        try:
            # URL 파싱
            cafe_info = parse_naver_cafe_url(cafe_url)
            
            # 정보 표시
            st.subheader("URL 정보")
            st.json(cafe_info)
            
            # 모바일 뷰어 링크 생성
            mobile_url = f"https://m.cafe.naver.com/{cafe_info['cafe_id']}/{cafe_info['article_id']}"
            st.subheader("모바일 뷰어 링크")
            st.markdown(f"[모바일에서 보기]({mobile_url})")
            
            # PC 뷰어 프레임
            st.subheader("PC 뷰어")
            pc_url = f"https://cafe.naver.com/{cafe_info['cafe_id']}/{cafe_info['article_id']}"
            st.markdown(
                f'<iframe src="{pc_url}" width="100%" height="600px"></iframe>',
                unsafe_allow_html=True
            )
            
        except Exception as e:
            st.error(f"URL 처리 중 오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    create_viewer_app()

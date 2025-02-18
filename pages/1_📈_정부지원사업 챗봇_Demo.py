import streamlit as st
from helper import get_chatbot_response
import json
import pathlib
import os

# 페이지 설정
st.set_page_config(page_title="AI 지원사업 챗봇", page_icon="🤖", layout="wide")

# 제목
st.title("🤖 AI 지원사업 챗봇")

# iframe 높이 조정 및 스타일 수정
st.components.v1.iframe(
    src="https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0",
    height=700,
    scrolling=True
)

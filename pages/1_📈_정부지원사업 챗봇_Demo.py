import streamlit as st
from helper import get_chatbot_response
import json
import pathlib
import os

# 페이지 설정
st.set_page_config(page_title="시흥XZ청년단 AI 지원사업 챗봇", page_icon="🤖", layout="wide")

# 제목
st.markdown("# 🤖 AI 지원사업 챗봇")

# 챗봇 iframe
st.markdown(
    '''
    <iframe
    src="https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0"
    style="width: 100%; height: 100%; min-height: 700px"
    frameborder="0"
    allow="microphone">
    </iframe>
    ''',
    unsafe_allow_html=True,
)

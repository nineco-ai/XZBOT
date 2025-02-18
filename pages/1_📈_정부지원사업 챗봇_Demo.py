import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="시흥XZ청년단 AI 지원사업 챗봇", 
    page_icon="🤖",
    layout="wide"
)

st.markdown("# 시흥XZ청년단 AI 지원사업 챗봇")

# Dify 챗봇 임베드
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        #dify-chatbot-container {
            width: 100%;
            height: 700px;
            border: none;
        }
    </style>
</head>
<body>
    <div style="width: 100%; height: 700px;">
        <iframe
            src="https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0"
            width="100%"
            height="100%"
            frameborder="0"
            allow="microphone"
        ></iframe>
    </div>
</body>
</html>
"""

# 챗봇 컨테이너 렌더링
components.html(
    html_code,
    height=750,
    scrolling=False
)

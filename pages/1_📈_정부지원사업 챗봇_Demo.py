import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="시흥XZ청년단 AI 지원사업 챗봇", 
    page_icon="🤖",
    layout="wide"
)

st.markdown("# AI 지원사업 챗봇")

# Dify 챗봇 스크립트와 함께 iframe 임베딩
html_code = """
<div style="width: 100%; height: 700px;">
    <script type="module">
        import { DifyQAWidget } from 'https://cdn.jsdelivr.net/npm/@dify/qt-web@0.0.1-rc.0/dist/qt-web.js'
        new DifyQAWidget({
            api: 'https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0',
            container: '#dify-chatbot-container',
            styles: {
                container: {
                    width: '100%',
                    height: '100%',
                }
            }
        })
    </script>
    <div id="dify-chatbot-container"></div>
</div>
"""

components.html(
    html_code,
    height=720,
)

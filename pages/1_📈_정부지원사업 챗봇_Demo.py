import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="AI 지원사업 챗봇", 
    page_icon="🤖",
    layout="wide"
)

st.markdown("# AI 지원사업 챗봇")

# Dify 챗봇 임베드
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
    <script src="https://cdn.jsdelivr.net/npm/@dify/qt-web@0.0.1-rc.0/dist/qt-web.umd.js"></script>
    <div id="dify-chatbot-container"></div>
    <script>
        DifyQAWidget.init({
            api: "https://web-production-b892.up.railway.app",
            accessToken: "2cuVKnu03YsqCuZ0",
            containerSelector: "#dify-chatbot-container",
            height: "700px",
        });
    </script>
</body>
</html>
"""

# 챗봇 컨테이너 렌더링
try:
    components.html(
        html_code,
        height=750,
        scrolling=True
    )
except Exception as e:
    st.error("챗봇 로딩 중 오류가 발생했습니다.")
    st.write("오류 내용:", str(e))

# 문제 발생 시 직접 링크 제공
st.markdown("""
---
챗봇이 보이지 않는 경우 [여기를 클릭하여 직접 접속](https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0)하실 수 있습니다.
""")

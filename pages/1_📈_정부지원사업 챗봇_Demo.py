import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정 (최상단에 위치해야 합니다)
st.set_page_config(
    page_title="시흥XZ청년단 AI 지원사업 챗봇",
    page_icon="🤖",
    layout="wide"
)

# 사이드바 설정: 챗봇 관련 정보만 표시
with st.sidebar:
    st.success("AI 지원사업 챗봇 안내")
    st.markdown("---")
    st.markdown(
        """
        ### 챗봇 사용 방법
        1. 궁금하신 지원사업에 대해 질문해 주세요.
        2. 가능한 구체적으로 질문해 주시면 더 정확한 답변을 받으실 수 있습니다.
        3. 챗봇이 로딩되지 않는 경우 페이지를 새로고침 해주세요.
        """
    )

# 메인 페이지 타이틀 (st.title 사용)
st.title("시흥XZ청년단 AI 지원사업 챗봇")

# Dify 챗봇 임베드 HTML 코드
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
components.html(html_code, height=750, scrolling=False)

# 문제 발생 시 대체 링크 제공
st.markdown(
    """
---
챗봇이 보이지 않는 경우 [여기를 클릭하여 직접 접속](https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0)하실 수 있습니다.
    """
)

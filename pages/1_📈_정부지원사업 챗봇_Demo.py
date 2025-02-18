import streamlit as st

# 페이지 설정
st.set_page_config(page_title="시흥XZ청년단 AI 지원사업 챗봇", page_icon="🤖", layout="wide")

# 제목
st.title("🤖 AI 지원사업 챗봇")

# iframe 직접 삽입
st.markdown(
    """
    <div style="width:100%; height:700px;">
        <iframe
            src="https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0"
            width="100%"
            height="100%"
            frameborder="0"
            allow="microphone">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

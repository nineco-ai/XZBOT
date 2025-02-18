import streamlit as st

st.set_page_config(page_title="Chatbot Demo", page_icon="🤖")

st.title("Chatbot Demo")

# iframe을 HTML로 직접 삽입
st.markdown(
    """
    <iframe
        src="https://web-production-b892.up.railway.app/chat/2cuVKnu03YsqCuZ0"
        style="width: 100%; height: 100%; min-height: 700px;"
        frameborder="0"
        allow="microphone"
    >
    </iframe>
    """,
    unsafe_allow_html=True,  # HTML 삽입 허용
)

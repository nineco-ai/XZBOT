import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Chatbot Demo", page_icon="🤖")

st.title("Chatbot Demo")

# iframe을 streamlit.components.v1.html로 삽입
components.html(
    """
    <iframe
        src="https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0"
        style="width: 100%; height: 100%; min-height: 700px;"
        frameborder="0"
        allow="microphone"
    >
    </iframe>
    """,
    height=700,
    scrolling=True
)

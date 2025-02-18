
import streamlit as st
st.set_page_config(page_title="시흥XZ청년단 AI 지원사업 챗봇", page_icon="🤖")
st.markdown("# AI 지원사업 챗봇")
def chatbot_response(user_input, context):
    responses = {
        "이 데모는 무엇인가요?": "이 데모는 정부지원사업에 대하여 사업자가 원하는 지원사업을 찾아주는 AI 챗봇입니다.",
        "어떻게 작동하나요?": "현재 사업규모나 형태를 입력하고 원하시는 지원사업을 입력해 주시면 원하시는 지원사업을 찾아드립니다.",
        "시흥XZ청년단의 AI 지원사업은 무엇인가요?": "관공서에서 나오는 지원사업을 맞춤형으로 매칭시켜주는 시스템 입니다..",
    }

    if context:
        return f"컨텍스트: {context}에 대한 질문입니다. " + responses.get(user_input, "죄송합니다, 그 질문에 대한 답변을 찾을 수 없습니다.")

    return responses.get(user_input, "죄송합니다, 그 질문에 대한 답변을 찾을 수 없습니다.")
# 사이드바에 컨텍스트 입력 추가
context_input = st.sidebar.text_area("컨텍스트를 입력하세요:", height=100)
# 챗봇 인터페이스 추가
st.header("챗봇")
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

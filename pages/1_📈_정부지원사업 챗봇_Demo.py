import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def init_session_state():
    """세션 상태 초기화"""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'context' not in st.session_state:
        st.session_state.context = ""

def update_context(new_context):
    """컨텍스트 업데이트"""
    st.session_state.context = new_context

def chatbot_response(user_input, context):
    """챗봇 응답 생성"""
    responses = {
        "이 데모는 무엇인가요?": "이 데모는 정부지원사업에 대하여 사업자가 원하는 지원사업을 찾아주는 AI 챗봇입니다.",
        "어떻게 작동하나요?": "현재 사업규모나 형태를 입력하고 원하시는 지원사업을 입력해 주시면 원하시는 지원사업을 찾아드립니다.",
        "시흥XZ청년단의 AI 지원사업은 무엇인가요?": "관공서에서 나오는 지원사업을 맞춤형으로 매칭시켜주는 시스템 입니다.",
    }
    
    if context:
        response = f"컨텍스트: {context}에 대한 질문입니다. " + responses.get(user_input, "죄송합니다, 그 질문에 대한 답변을 찾을 수 없습니다.")
    else:
        response = responses.get(user_input, "죄송합니다, 그 질문에 대한 답변을 찾을 수 없습니다.")
    
    st.session_state.chat_history.append({"user": user_input, "bot": response})
    return response

def main():
    # 세션 상태 초기화
    init_session_state()
    
    # 페이지 설정
    st.set_page_config(
        page_title="AI 지원사업 챗봇",
        page_icon="🤖",
        layout="wide"
    )
    
    # CSS 스타일
    st.markdown("""
        <style>
        .stApp {
            max-width: 100%;
            padding: 1rem;
        }
        .chat-container {
            margin: 1rem 0;
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #f8f9fa;
        }
        .iframe-container {
            width: 100%;
            height: 700px;
            margin: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # 제목
    st.markdown("# AI 지원사업 챗봇 🤖")
    
    # 사이드바
    with st.sidebar:
        st.header("설정")
        new_context = st.text_area(
            "컨텍스트를 입력하세요:",
            value=st.session_state.context,
            height=100,
            key="context_input"
        )
        if new_context != st.session_state.context:
            update_context(new_context)
    
    # 메인 챗봇 인터페이스
    st.header("챗봇 인터페이스")
    
    # iframe 컨테이너
    st.markdown(
        '''
        <div class="iframe-container">
            <iframe
                src="https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0"
                style="width: 100%; height: 100%;"
                frameborder="0"
                allow="microphone"
                id="chatbot-iframe">
            </iframe>
        </div>
        ''',
        unsafe_allow_html=True
    )
    
    # 채팅 히스토리 표시
    if st.session_state.chat_history:
        st.markdown("### 대화 기록")
        for chat in st.session_state.chat_history:
            st.markdown(f"**사용자:** {chat['user']}")
            st.markdown(f"**챗봇:** {chat['bot']}")
            st.markdown("---")

if __name__ == "__main__":
    main()

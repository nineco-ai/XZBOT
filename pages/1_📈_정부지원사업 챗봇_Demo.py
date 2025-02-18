import streamlit as st
from streamlit.logger import get_logger
import streamlit.components.v1 as components

LOGGER = get_logger(__name__)

def init_session_state():
    """세션 상태 초기화"""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'context' not in st.session_state:
        st.session_state.context = ""

def main():
    # 세션 상태 초기화
    init_session_state()
    
    # 페이지 설정
    st.set_page_config(
        page_title="AI 지원사업 챗봇",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # CSS 스타일
    st.markdown("""
        <style>
        .stApp {
            max-width: 100%;
            padding: 0;
        }
        .main .block-container {
            max-width: 100%;
            padding: 2rem;
        }
        .info-box {
            background-color: #f8f9fa;
            border-left: 4px solid #1f77b4;
            padding: 1.5rem;
            margin: 1rem 0;
            border-radius: 0 4px 4px 0;
        }
        .info-box h4 {
            color: #1f77b4;
            margin-bottom: 0.8rem;
            font-size: 1.2rem;
            font-weight: 600;
        }
        .info-box p {
            color: #2c3e50;
            line-height: 1.6;
            font-size: 1rem;
        }
        .project-status {
            background-color: #e1f5fe;
            border-radius: 8px;
            padding: 1.5rem;
            margin-top: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .project-status h4 {
            color: #0277bd;
            margin-bottom: 0.8rem;
            font-size: 1.2rem;
            font-weight: 600;
        }
        .project-status p {
            color: #1a237e;
            line-height: 1.6;
            font-size: 1rem;
        }
        [data-testid="stSidebar"] {
            min-width: 300px;
            max-width: 400px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # 제목
    st.markdown("# AI 지원사업 챗봇 🤖")
    
    # 사이드바
    with st.sidebar:
        st.header("설정")
        context = st.text_area(
            "컨텍스트를 입력하세요:",
            value=st.session_state.context,
            height=100,
            key="context_input"
        )
    
    # 챗봇 인터페이스를 먼저 표시
    st.header("챗봇 인터페이스")
    
    # iframe을 직접 HTML로 삽입
    html_code = """
        <div style="width: 100%; height: 800px; padding: 0; border-radius: 10px; overflow: hidden; margin: 1rem 0; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <iframe 
                src="https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0"
                width="100%"
                height="100%"
                frameborder="0"
                allow="microphone"
                style="width: 1px; min-width: 100%; height: 100%; min-height: 800px;"
                sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
            </iframe>
        </div>
    """
    
    # iframe 표시
    components.html(
        html_code,
        height=850,
        scrolling=True
    )
    
    # 프로젝트 소개
    st.markdown("### 프로젝트 소개")
    st.markdown(
        """
        <div class="info-box">
            <h4>데모 페이지 소개</h4>
            <p>이 챗봇은 현재까지 공개된 지원사업을 매일 수집하여 분류하고 검색하는 기능을 시연하기 위해 제작된 데모 페이지입니다.</p>
        </div>
        
        <div class="project-status">
            <h4>🚀 현재 진행 중인 프로젝트</h4>
            <p>시흥XZ청년단은 현재 각 회원사의 특성과 필요에 맞는 맞춤형 지원사업 매칭 서비스를 개발하고 있습니다. 
            이를 통해 회원사들에게 더욱 정확하고 효율적인 지원사업 정보를 제공할 예정입니다.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 설명 섹션
    with st.expander("챗봇 사용 방법"):
        st.markdown("""
        1. 챗봇에 원하시는 질문을 입력해주세요
        2. 지원사업 관련 정보를 얻으실 수 있습니다
        3. 추가 질문이나 상세 정보가 필요하시면 더 자세히 물어보실 수 있습니다
        """)

if __name__ == "__main__":
    main()

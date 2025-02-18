import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="시흥XZ청년단 AI 지원사업 챗봇",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS 추가
st.markdown("""
    <style>
        /* 전체 페이지 스타일 */
        .stApp {
            background-color: white !important;
        }
        
        /* 컨테이너 스타일 */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 100%;
        }
        
        /* iframe 컨테이너 스타일 */
        .iframe-container {
            background-color: white;
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* 섹션 스타일 */
        .section {
            padding: 1rem;
            margin: 1rem 0;
            background-color: white;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# 제목
st.title("AI 지원사업 챗봇 🤖")

# iframe을 try-except로 감싸서 에러 처리
try:
    # 1. iframe 챗봇
    st.markdown('<div class="iframe-container">', unsafe_allow_html=True)
    components.html(
        f'''
        <iframe 
            src="https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0"
            width="100%"
            height="700"
            style="border: none; background-color: white;"
            allow="microphone *"
            sandbox="allow-same-origin allow-scripts allow-popups allow-forms allow-downloads"
        ></iframe>
        ''',
        height=720,
        scrolling=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
except Exception as e:
    st.error(f"""
        챗봇 로딩 중 문제가 발생했습니다. 잠시 후 다시 시도해주세요.
        
        임시 해결방법:
        1. 페이지 새로고침
        2. 브라우저 캐시 삭제
        3. 다른 브라우저로 접속
    """)
    st.error(f"에러 상세: {str(e)}")

# 2. 챗봇 사용방법
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("💡 챗봇 사용방법")
    st.write("""
    1. 챗봇에 원하시는 질문을 입력해주세요
    2. 지원사업 관련 정보를 얻으실 수 있습니다
    3. 추가 질문이나 상세 정보가 필요하시면 더 자세히 물어보실 수 있습니다
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# 3. 데모 페이지 소개
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("📌 데모 페이지 소개")
    st.write("""
    이 챗봇은 현재까지 공개된 지원사업을 매일 수집하여 분류하고 검색하는 기능을 
    시연하기 위해 제작된 데모 페이지입니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# 4. 현재 진행중인 프로젝트
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("🚀 현재 진행 중인 프로젝트")
    st.info("""
    시흥XZ청년단은 현재 각 회원사의 특성과 필요에 맞는 맞춤형 지원사업 매칭 서비스를 개발하고 있습니다.
    이를 통해 회원사들에게 더욱 정확하고 효율적인 지원사업 정보를 제공할 예정입니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

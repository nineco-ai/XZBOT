import streamlit as st
from datetime import datetime

# 현재 시간을 이용한 버전 관리
VERSION = datetime.now().strftime("%Y%m%d%H%M%S")

# 페이지 설정
st.set_page_config(
    page_title="AI 지원사업 챗봇",
    page_icon="🤖",
    layout="wide"
)

# 상태 초기화
if 'version' not in st.session_state:
    st.session_state.version = VERSION

# CSS 스타일 (버전 포함)
st.markdown(f"""
    <style>
    /* Version: {VERSION} */
    .stApp {{
        max-width: 100%;
    }}
    .chat-container {{
        margin: 1rem 0;
        padding: 1rem;
    }}
    .info-section {{
        margin: 2rem 0;
        padding: 1rem;
        background-color: #f8f9fa;
        border-radius: 8px;
    }}
    .version-info {{
        display: none;
    }}
    </style>
""", unsafe_allow_html=True)

# 버전 정보 (디버깅용, 숨김)
st.markdown(f'<div class="version-info">Version: {VERSION}</div>', unsafe_allow_html=True)

# 제목
st.title("AI 지원사업 챗봇 🤖")

# 1. 챗봇 iframe (버전 파라미터 추가)
st.header("챗봇")
st.markdown(
    f'''
    <iframe
        src="https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0?v={VERSION}"
        style="width: 100%; height: 100%; min-height: 700px"
        frameborder="0"
        allow="microphone">
    </iframe>
    ''',
    unsafe_allow_html=True,
)

# 2. 챗봇 사용방법
st.markdown(f"""
    <div class="info-section">
        <h3>💡 챗봇 사용방법</h3>
        <ol>
            <li>챗봇에 원하시는 질문을 입력해주세요</li>
            <li>지원사업 관련 정보를 얻으실 수 있습니다</li>
            <li>추가 질문이나 상세 정보가 필요하시면 더 자세히 물어보실 수 있습니다</li>
        </ol>
    </div>
""", unsafe_allow_html=True)

# 3. 데모 페이지 소개
st.markdown(f"""
    <div class="info-section">
        <h3>📌 데모 페이지 소개</h3>
        <p>이 챗봇은 현재까지 공개된 지원사업을 매일 수집하여 분류하고 검색하는 기능을 시연하기 위해 제작된 데모 페이지입니다.</p>
    </div>
""", unsafe_allow_html=True)

# 4. 현재 진행중인 프로젝트
st.markdown(f"""
    <div class="info-section" style="background-color: #e1f5fe;">
        <h3>🚀 현재 진행 중인 프로젝트</h3>
        <p>시흥XZ청년단은 현재 각 회원사의 특성과 필요에 맞는 맞춤형 지원사업 매칭 서비스를 개발하고 있습니다. 
        이를 통해 회원사들에게 더욱 정확하고 효율적인 지원사업 정보를 제공할 예정입니다.</p>
    </div>
""", unsafe_allow_html=True)

# 캐시 제어를 위한 메타 태그 추가
st.markdown("""
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
""", unsafe_allow_html=True)

# 재실행 버튼 (디버깅용)
if st.button("새로고침"):
    st.session_state.version = datetime.now().strftime("%Y%m%d%H%M%S")
    st.experimental_rerun()

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def init_session_state():
    """세션 상태 초기화 함수"""
    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False
    if 'name' not in st.session_state:
        st.session_state.name = ""
    if 'email' not in st.session_state:
        st.session_state.email = ""
    if 'phone' not in st.session_state:
        st.session_state.phone = ""
    if 'message' not in st.session_state:
        st.session_state.message = ""

def handle_form_submission():
    """폼 제출 처리 함수"""
    st.session_state.form_submitted = True
    # 여기에 실제 폼 데이터 처리 로직 추가

def run():
    # 세션 상태 초기화
    init_session_state()
    
    # 페이지 기본 설정
    st.set_page_config(
        page_title="시흥XZ청년단",
        page_icon="👋",
        layout="wide"  # 전체 화면 레이아웃 사용
    )
    
    # CSS 스타일 추가 - !important 추가하여 스타일 우선순위 높임
    st.markdown("""
        <style>
        .section-divider {
            margin-top: 2rem !important;
            margin-bottom: 2rem !important;
            border-top: 2px solid #f0f2f6 !important;
        }
        .feature-container {
            padding: 1rem !important;
            border-radius: 0.5rem !important;
            background-color: #f8f9fa !important;
            margin-bottom: 1rem !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        }
        .stButton > button {
            width: 100% !important;
            margin-top: 1rem !important;
        }
        .streamlit-expanderHeader {
            background-color: #f8f9fa !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # 사이드바
    with st.sidebar:
        st.success("현재 페이지는 시흥XZ청년단 AI 챗봇 데모 페이지입니다.")
        st.markdown("---")
        st.markdown("### 빠른 링크")
        st.markdown("[🏠 네이버 카페](https://cafe.naver.com/xzceo)")
        st.markdown("[📄 리플릿 보기](https://drive.google.com/file/d/1mSfk93qD_hzHlKJgVp5gXL3hfvGY5WYl/view)")
    
    # 메인 콘텐츠
    st.write("# 시흥XZ청년단에 오신것을 환영합니다! 👋")
    
    with st.container():
        st.markdown(
            """
            시흥시의 미래를 선도하는 젊은 기업가들의 모임입니다.  
            X세대부터 Z세대까지 시흥시 관내의 청년기업가들이 함께합니다.
            
            ### 우리의 비전
            시흥시 관내 청년 기업가, 창업가, 예비창업자들 간의 정보 교류와 협력을 통해
            현재의 성장을 함께 공유하고, 미래를 주도하는 기업으로 성장하고자 합니다.
            """
        )
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # 특징 섹션
    st.header("📌 주요 특징")
    
    cols = st.columns(3)
    features = [
        {
            "title": "🎯 우리의 미션",
            "content": """
            - 시흥시 청년기업 성장 지원
            - 기업간 정보 교류 활성화
            - 상생 협력 네트워크 구축
            """
        },
        {
            "title": "🤝 참여 대상",
            "content": """
            - 시흥시 청년 기업가
            - 예비 창업자
            - 관내 청년 사업가
            """
        },
        {
            "title": "💡 주요 활동",
            "content": """
            - 기업간 정보 교류
            - 성장 경험 공유
            - 협력 프로젝트 추진
            """
        }
    ]
    
    for col, feature in zip(cols, features):
        with col:
            with st.container():
                st.markdown(f'<div class="feature-container">', unsafe_allow_html=True)
                st.markdown(f"### {feature['title']}")
                st.markdown(feature['content'])
                st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # 문의하기 폼
    st.header("✉️ 문의하기")
    
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("이름", key="name_input")
            email = st.text_input("이메일", key="email_input")
            phone = st.text_input("연락처", key="phone_input")
        
        with col2:
            category = st.selectbox(
                "문의 유형",
                ["가입 문의", "협력 제안", "기타 문의"],
                key="category_input"
            )
            message = st.text_area("문의 내용", key="message_input")
        
        submitted = st.form_submit_button("문의하기")
        if submitted:
            # 폼 제출 처리
            handle_form_submission()
            st.success("문의가 접수되었습니다. 확인 후 연락드리겠습니다.")
            # 폼 초기화
            st.session_state.name = ""
            st.session_state.email = ""
            st.session_state.phone = ""
            st.session_state.message = ""

if __name__ == "__main__":
    run()

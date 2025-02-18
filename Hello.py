import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    # 페이지 기본 설정
    st.set_page_config(
        page_title="시흥XZ청년단",
        page_icon="👋",
    )

    # 사이드바
    st.sidebar.success("현재 페이지는 시흥XZ청년단 AI 챗봇 데모 페이지입니다.")

    # 메인 헤더
    st.write("# 시흥XZ청년단에 오신것을 환영합니다! 👋")

    # 메인 콘텐츠
    st.markdown(
        """
        시흥시의 미래를 선도하는 젊은 기업가  
        X세대부터 Z세대까지 시흥시 관내의 청년기업가 모임

        시흥시 관내에 청년 기업가, 창업가, 예비창업자들에게 선후배 기업간의
        정보, 교류를 통해 현재의 성장을 함께 공유하고, 미래를 주도하는 기업으로 나가가기
        위한 상생 협력 단체를 만들고자 한다.

        ### XZ청년단 커뮤니티 소개 
        - [시흥XZ청년단 네이버 카페](https://cafe.naver.com/xzceo)
        - [시흥XZ청년단 리플릿](https://drive.google.com/file/d/1mSfk93qD_hzHlKJgVp5gXL3hfvGY5WYl/view)
        """
    )

    # 추가 정보 섹션
    st.markdown("---")
    
    # 3개 컬럼으로 주요 특징 표시
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🎯 우리의 미션")
        st.write("""
        - 시흥시 청년기업 성장 지원
        - 기업간 정보 교류 활성화
        - 상생 협력 네트워크 구축
        """)

    with col2:
        st.markdown("### 🤝 참여 대상")
        st.write("""
        - 시흥시 청년 기업가
        - 예비 창업자
        - 관내 청년 사업가
        """)

    with col3:
        st.markdown("### 💡 주요 활동")
        st.write("""
        - 기업간 정보 교류
        - 성장 경험 공유
        - 협력 프로젝트 추진
        """)

    # 문의하기 섹션
    st.markdown("---")
    st.markdown("### ✉️ 문의하기")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("이름")
        email = st.text_input("이메일")
        phone = st.text_input("연락처")
    
    with col2:
        category = st.selectbox(
            "문의 유형",
            ["가입 문의", "협력 제안", "기타 문의"]
        )
        message = st.text_area("문의 내용")
    
    if st.button("문의하기"):
        st.success("문의가 접수되었습니다. 확인 후 연락드리겠습니다.")

if __name__ == "__main__":
    run()

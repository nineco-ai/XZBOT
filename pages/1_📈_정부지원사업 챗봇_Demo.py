import streamlit as st

st.set_page_config(page_title="시흥XZ청년단 정부지원사업 AI", page_icon="🤖")

st.title("시흥XZ청년단 정부지원사업 AI")

# iframe을 HTML로 직접 삽입 (이 부분은 그대로 유지)
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

# 추가 섹션들

st.header("챗봇 사용방법")
st.write("""
- 챗봇에 원하시는 질문을 입력해주세요  
- 지원사업 관련 정보를 얻으실 수 있습니다  
- 추가 질문이나 상세 정보가 필요하시면 더 자세히 물어보실 수 있습니다
""")

st.header("데모 페이지 소개")
st.write("""
이 챗봇은 현재까지 공개된 지원사업을 매일 수집하여 분류하고 검색하는 기능을 시연하기 위해 제작된 데모 페이지입니다.
""")

st.header("현재 진행중인 프로젝트")
st.write("""
시흥XZ청년단은 현재 각 회원사의 특성과 필요에 맞는 맞춤형 지원사업 매칭 서비스를 개발하고 있습니다. 
이를 통해 회원사들에게 더욱 정확하고 효율적인 지원사업 정보를 제공할 예정입니다.
""")

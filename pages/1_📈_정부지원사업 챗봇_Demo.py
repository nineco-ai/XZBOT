import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="시흥XZ청년단 AI 지원사업 챗봇",
    page_icon="🤖",
    layout="wide"
)

# 제목
st.title("AI 지원사업 챗봇 🤖")

# CSS 추가
st.markdown("""
    <style>
        .element-container {
            width: 100%;
        }
        iframe {
            width: 100%;
            min-height: 700px;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# 1. iframe 챗봇
html_content = """
<iframe 
    src="https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0" 
    style="width: 100%; height: 100%; min-height: 700px;" 
    frameborder="0" 
    allow="microphone">
</iframe>
"""
components.html(html_content, height=700)

# 2. 챗봇 사용방법
st.header("💡 챗봇 사용방법")
st.write("""
1. 챗봇에 원하시는 질문을 입력해주세요
2. 지원사업 관련 정보를 얻으실 수 있습니다
3. 추가 질문이나 상세 정보가 필요하시면 더 자세히 물어보실 수 있습니다
""")

# 3. 데모 페이지 소개
st.header("📌 데모 페이지 소개")
st.write("""
이 챗봇은 현재까지 공개된 지원사업을 매일 수집하여 분류하고 검색하는 기능을 
시연하기 위해 제작된 데모 페이지입니다.
""")

# 4. 현재 진행중인 프로젝트
st.header("🚀 현재 진행 중인 프로젝트")
st.info("""
시흥XZ청년단은 현재 각 회원사의 특성과 필요에 맞는 맞춤형 지원사업 매칭 서비스를 개발하고 있습니다.
이를 통해 회원사들에게 더욱 정확하고 효율적인 지원사업 정보를 제공할 예정입니다.
""")

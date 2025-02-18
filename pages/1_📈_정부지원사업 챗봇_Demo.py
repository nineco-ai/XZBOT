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

# 추가된 섹션들
st.header("2. 챗봇 사용방법")
st.write("""
- 챗봇에 원하시는 질문을 입력해주세요
- 지원사업 관련 정보를 얻으실 수 있습니다
- 추가 질문이나 상세 정보가 필요하시면 더 자세히 물어보실 수 있습니다
""")

st.header("3. 데모 페이지 소개")
st.write("""
이 챗봇은 현재까지 공개된 지원사업을 매일 수집하여 분류하고 검색하는 기능을 시연하기 위해 제작된 데모 페이지입니다.
""")

st.header("4. 현재 진행중인 프로젝트")
st.write("""
시흥XZ청년단은 현재 각 회원사의 특성과 필요에 맞는 맞춤형 지원사업 매칭 서비스를 개발하고 있습니다. 
이를 통해 회원사들에게 더욱 정확하고 효율적인 지원사업 정보를 제공할 예정입니다.
""")

import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="AI 지원사업 챗봇", 
    page_icon="🤖",
    layout="wide"  # 전체 화면 너비 사용
)

st.markdown("# AI 지원사업 챗봇")

def chatbot_response(user_input, context):
    responses = {
        "이 데모는 무엇인가요?": "이 데모는 정부지원사업에 대하여 사업자가 원하는 지원사업을 찾아주는 AI 챗봇입니다.",
        "어떻게 작동하나요?": "현재 사업규모나 형태를 입력하고 원하시는 지원사업을 입력해 주시면 원하시는 지원사업을 찾아드립니다.",
        "시흥XZ청년단의 AI 지원사업은 무엇인가요?": "관공서에서 나오는 지원사업을 맞춤형으로 매칭시켜주는 시스템 입니다.",
    }
    
    if context:
        return f"컨텍스트: {context}에 대한 질문입니다. " + responses.get(user_input, "죄송합니다, 그 질문에 대한 답변을 찾을 수 없습니다.")
    
    return responses.get(user_input, "죄송합니다, 그 질문에 대한 답변을 찾을 수 없습니다.")

# 사이드바에 컨텍스트 입력 추가
context_input = st.sidebar.text_area("컨텍스트를 입력하세요:", height=100)

# 챗봇 인터페이스 추가
st.header("챗봇")

# HTML wrapper와 함께 iframe 임베딩
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .iframe-container {
            position: relative;
            width: 100%;
            height: 700px;
            overflow: hidden;
        }
        .chatbot-iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }
    </style>
</head>
<body>
    <div class="iframe-container">
        <iframe 
            class="chatbot-iframe"
            src="https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0"
            allow="microphone"
            sandbox="allow-same-origin allow-scripts allow-forms allow-popups"
        ></iframe>
    </div>
</body>
</html>
"""

try:
    components.html(
        html_code,
        height=720,
        scrolling=True
    )
except Exception as e:
    st.error(f"챗봇 로딩 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.")
    st.write("오류 상세:", str(e))

# 에러 발생 시 대체 UI 표시
st.markdown("""
---
### 챗봇이 로딩되지 않는 경우:
1. 페이지를 새로고침 해보세요
2. 다른 브라우저로 접속해보세요
3. [직접 링크](https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0)로 접속해보세요
""")

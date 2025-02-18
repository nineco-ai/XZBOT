import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="AI 지원사업 챗봇", 
    page_icon="🤖",
    layout="wide"
)

# 사이드바 - 독립적으로 작동하는 간단한 Q&A 시스템
with st.sidebar:
    st.header("일반 문의")
    context_input = st.text_area("문의사항을 입력하세요:", height=100)
    if st.button("답변 받기"):
        if context_input:
            responses = {
                "이 데모는 무엇인가요?": "이 데모는 정부지원사업에 대하여 사업자가 원하는 지원사업을 찾아주는 AI 챗봇입니다.",
                "어떻게 작동하나요?": "현재 사업규모나 형태를 입력하고 원하시는 지원사업을 입력해 주시면 원하시는 지원사업을 찾아드립니다.",
                "시흥XZ청년단의 AI 지원사업은 무엇인가요?": "관공서에서 나오는 지원사업을 맞춤형으로 매칭시켜주는 시스템 입니다.",
            }
            response = responses.get(context_input, "죄송합니다, 해당 질문에 대한 답변을 찾을 수 없습니다.")
            st.write("답변:", response)

# 메인 영역 - Dify 챗봇
st.markdown("# AI 지원사업 챗봇")

# Dify 챗봇 임베드
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        #dify-chatbot-container {
            width: 100%;
            height: 700px;
            border: none;
        }
    </style>
</head>
<body>
    <div style="width: 100%; height: 700px;">
        <iframe
            src="https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0"
            width="100%"
            height="100%"
            frameborder="0"
            allow="microphone"
        ></iframe>
    </div>
</body>
</html>
"""

# 챗봇 컨테이너 렌더링
components.html(
    html_code,
    height=750,
    scrolling=False
)

# 오류 발생 시 대체 링크 제공
st.markdown("""
---
챗봇이 보이지 않는 경우 [여기를 클릭하여 직접 접속](https://web-production-b892.up.railway.app/chatbot/2cuVKnu03YsqCuZ0)하실 수 있습니다.
""")

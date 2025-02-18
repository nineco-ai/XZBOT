[이전 코드와 동일...]

def run():
    # 세션 상태 초기화
    init_session_state()
    
    # 페이지 기본 설정
    st.set_page_config(
        page_title="시흥XZ청년단",
        page_icon="👋",
        layout="wide"
    )
    
    [CSS 스타일 부분 동일...]
    
    # 사이드바
    with st.sidebar:
        st.success("현재 페이지는 시흥XZ청년단 AI 챗봇 데모 페이지입니다.")
        st.markdown("---")
        st.markdown("### 빠른 링크")
        st.markdown("[🏠 네이버 카페](https://cafe.naver.com/xzceo)")
        st.markdown("[📄 리플릿 보기](https://drive.google.com/file/d/1mSfk93qD_hzHlKJgVp5gXL3hfvGY5WYl/view)")
    
    # 메인 콘텐츠
    st.write("# 시흥XZ청년단에 오신것을 환영합니다! 👋")
    
    # AI 챗봇 섹션 추가
    st.header("🤖 AI 지원사업 챗봇")
    
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
    
    components.html(
        html_code,
        height=750,
        scrolling=False
    )
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    [나머지 코드 동일...]

if __name__ == "__main__":
    run()

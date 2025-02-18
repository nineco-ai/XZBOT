# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import inspect
import textwrap
import time
import numpy as np
from utils import show_code  # utils 모듈에 show_code 함수가 정의되어 있어야 합니다.

def plotting_demo():
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)
    
    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)
    
    progress_bar.empty()
    # 이 버튼을 누르면 스크립트가 다시 실행됩니다.
    st.button("Re-run")

def chatbot_response(user_input, context):
    responses = {
        "이 데모는 무엇인가요?": "이 데모는 정부지원사업에 대하여 사업자가 원하는 지원사업을 찾아주는 AI 챗봇입니다.",
        "어떻게 작동하나요?": "현재 사업규모나 형태를 입력하고 원하시는 지원사업을 입력해 주시면 원하시는 지원사업을 찾아드립니다.",
        "시흥XZ청년단의 AI 지원사업은 무엇인가요?": "관공서에서 나오는 지원사업을 맞춤형으로 매칭시켜주는 시스템 입니다..",
    }

    # 컨텍스트에 대한 답변 추가
    if context:
        return f"컨텍스트: {context}에 대한 질문입니다. " + responses.get(user_input, "죄송합니다, 그 질문에 대한 답변을 찾을 수 없습니다.")

    return responses.get(user_input, "죄송합니다, 그 질문에 대한 답변을 찾을 수 없습니다.")

# 페이지 설정
st.set_page_config(page_title="Plotting Demo", page_icon="📈")

# 메인 페이지 제목
st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

# 사이드바에 컨텍스트 입력 추가
context_input = st.sidebar.text_area("컨텍스트를 입력하세요:", height=100)

# 챗봇 인터페이스 추가 (iframe을 직접 HTML로 임베드)
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

# 플로팅 데모 실행
plotting_demo()

# 플로팅 데모 코드 보여주기 (utils 모듈에 show_code 함수가 정의되어 있어야 합니다.)
show_code(plotting_demo)

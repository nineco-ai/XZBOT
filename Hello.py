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
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="시흥XZ청년단",
        page_icon="👋",
    )

    st.write("# 시흥XZ청년단에 오신것을 환영합니다! 👋")

    st.sidebar.success("현재 페이지는 시흥XZ청년단 AI 챗봇 데모 페이지입니다.")

    st.markdown(
        """
        시흥시의 미래를 선도하는 젊은 기업가
        X세대부터 Z세대까지 시흥시 관내의 청년기업가 모임
        **👈 
        시흥시 관내에 청년 기업가, 창업가, 예비창업자들에게 선후배 기업간의
        정보, 교류를 통해 현재의 성장을 함께 공유하고, 미래를 주도하는 기업으로 나가가기
        위한 상생 협력 단체를 만들고자 한다.
        ### XZ청년단 커뮤니티 소개 
        - 시흥XZ청년단 네이버 카페 URL (https://cafe.naver.com/xzceo)
        - 시흥XZ청년단 리플릿 (https://drive.google.com/file/d/1mSfk93qD_hzHlKJgVp5gXL3hfvGY5WYl/view)
    """
    )


if __name__ == "__main__":
    run()
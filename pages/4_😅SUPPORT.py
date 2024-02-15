
from openai import OpenAI
import streamlit as st
# from streamlit_option_menu import option_menu
import time
# import toml
import os

OpenAI.api_key = st.secrets["key"]
file_id = st.secrets['file']
assistant_id = st.secrets['assistant_id']
thread_id = st.secrets['thread_id']

client = OpenAI(api_key = OpenAI.api_key)


def request_chat_completion(
        prompt, 
        system_role="당신은 매우 훌륭한 목회 도우미입니다.", 
        model="gpt-3.5-turbo", 
        stream=True
        ):
    # 사용자와 시스템 메시지를 포함한 대화를 구성
    messages = [
        {"role": "system", "content": system_role},
        {"role": "user", "content": prompt}
    ]

    # OpenAI API에 메시지 전송
    response = client.chat.completions.create(
        model=model, 
        messages=messages, 
        stream=stream)
client = OpenAI(api_key=st.secrets["key"])
file_id = st.secrets['file']
assistant_id = st.secrets['assistant_id']
thread_id = st.secrets['thread_id']

st.markdown("<h1 style='text-align: center; color: black;'>Chat Bot 인공지능 목회연구소</h1>", unsafe_allow_html=True)
# st.title("Chat Bot 인공지능 목회연구소")
# st.subheader("유료 API를 사용하고 있습니다")
# st.subheader("서비스 유지에 여러분의 도움이 간절히 필요합니다.")
st.markdown("<h2 style='text-align: center; color: red;'>유료 API를 사용하고 있습니다</h2>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: gray;'>서비스 유지에 여러분의 도움이 간절히 필요합니다.</h3>", unsafe_allow_html=True)

# st.text("카카오뱅크 3333-02-8468999")
st.markdown("<h2 style='text-align: center; color: black;'>카카오뱅크 3333-02-8468999 이승호</h2>", unsafe_allow_html=True)



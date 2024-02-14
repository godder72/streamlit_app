from openai import OpenAI
import streamlit as st
import time
import os


client = OpenAI(api_key=st.secrets["key"])
file_id = st.secrets['file']
assistant_id = st.secrets['assistant_id']
thread_id = st.secrets['thread_id']

st.markdown("<h1 style='text-align: center; color: black;'>Chat Bot 인공지능 목회연구소</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>💖 저는 인공지능 목회 도우미입니다</h3>", unsafe_allow_html=True)
# st.title("Chat Bot 인공지능 목회연구소")
# st.subheader("💖 저는 인공지능 목회 도우미입니다")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "무엇을 도와드릴까요?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

################# thread 에 대화를 저장 ######

    response = client.beta.threads.messages.create(thread_id, role="user", content=prompt)

    run = client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id)

    run_id = run.id

    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        if run.status == "completed":
            break
        else:
            time.sleep(1)
        # print(run)

    thread_messages = client.beta.threads.messages.list(thread_id)

    msg = thread_messages.data[0].content[0].text.value

############## thread 에 대화를 저장 ##########

    st.session_state.messages.append({"role":"assistant", "content": msg})
    st.chat_message("assistant").write(msg)

        
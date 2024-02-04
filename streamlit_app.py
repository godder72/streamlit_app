
from openai import OpenAI
import streamlit as st
from streamlit_option_menu import option_menu
import time
import os


openai_api_key = os.environ["openai_api_key"]


file = "file-xfFe9kHyuV8m1MRDNUgsdlBZ"
assistant_id = "asst_o6ct3M2Ot3sBn56G3U3pqh9S"
thread_id = "thread_5iXWqxm8uiqNBf8MdZUMATnc"

with st.sidebar:
    st.title('인공지능 목회연구소')
    selected = option_menu(
        menu_title = "Chat Bot", 
        options=["NONE1", "NONE2", "NONE3"],
        icons=["house", "robot", "envelope"],
        menu_icon = "cast",
        default_index=0,
        # orientation="horizontal"
    )


if selected == "NONE1":
    st.title(f"")
if selected == "NONE2":
    st.title(f"You Selected {selected}")
if selected == "NONE3":
    st.title(f"You Selected {selected}")

client = OpenAI(api_key = openai_api_key)

if "messages" not in st.session_state:
    st.title("💬 Chatbot _ 인공지능 목회 연구소") 

st.session_state["messages"] = [{"role": "assistant", "content": "저는 목회 비서라고 합니다. 무엇을 도와드릴까요?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    if not thread_id:
        st.info("Please add your Thread ID to continue.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})

    st.chat_message("user").write(prompt)

###############33
    response = client.beta.threads.messages.create(
    thread_id,
    role="user",
    content=prompt,
    )


#################
    run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id
    )
    # print(run)

    run_id = run.id
    while True:
            
        run = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
        )
        if run.status == "completed":
            break
        else:
            time.sleep(2)
    
    thread_messages = client.beta.threads.messages.list(thread_id)
    print(thread_messages.data)

    msg = thread_messages.data[0].content[0].text.value
    print(msg)

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

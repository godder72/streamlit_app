# First
from openai import OpenAI
import streamlit as st
from streamlit_option_menu import option_menu
import time


my_personal_api_key = "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"
file = "file-xfFe9kHyuV8m1MRDNUgsdlBZ"
# 아래 어시스턴트 아이디는 위의 파일을 기준으로 만든 것임. 따라서, 어시스탄트에 파일을 추가하는 방법을 확인해야돼. 

assistant_id = "asst_o6ct3M2Ot3sBn56G3U3pqh9S"
thread_id = "thread_5iXWqxm8uiqNBf8MdZUMATnc"





client = OpenAI(api_key = my_personal_api_key)


with st.sidebar:
    # st.title('Chat Bot')
    st.title('인공지능 목회연구소')
    openai_api_key = my_personal_api_key

    selected = option_menu(
        menu_title = "Chat Bot", 
        options=["home", "project", "contact"],
        icons=["house", "robot", "envelope"],
        menu_icon = "cast",
        default_index=0,
        # orientation="horizontal"
    )

if selected == "home":
    st.title(f"You Selected {selected}")
if selected == "project":
    st.title(f"You Selected {selected}")
if selected == "contact":
    st.title(f"You Selected {selected}")



    # thread_id = st.text_input("Thread ID")
    # thread_btn = st.button("Create a new thread")

    # if thread_btn:
    #     thread = client.beta.threads.create()
    #     thread_id = thread.id

    #     st. subheader(f"{thread_id}", divider='rainbow')
    #     st. info("스레드를 생성합니다.")



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

    # response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)

    # msg = response.choices[0].message.content

    # st.session_state.messages.append({"role": "assistant", "content": prompt})
    # st.chat_message("assistant").write(prompt)

###############33
    response = client.beta.threads.messages.create(
    thread_id,
    role="user",
    content=prompt,
    )
    print(response)


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
        print(run)

    thread_messages = client.beta.threads.messages.list(thread_id)
    print(thread_messages.data)

    msg = thread_messages.data[0].content[0].text.value
    print(msg)

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)





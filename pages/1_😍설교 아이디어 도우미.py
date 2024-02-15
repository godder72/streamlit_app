
from openai import OpenAI
import streamlit as st



file_id = st.secrets['file']
assistant_id = st.secrets['assistant_id']
thread_id = st.secrets['thread_id']

client = OpenAI(api_key = st.secrets["key"])


def request_chat_completion(prompt,system_role="당신은 매우 훌륭한 목회 도우미입니다.",model="gpt-3.5-turbo",stream=True):

    messages = [{"role": "system", "content": system_role}, {"role": "user", "content": prompt}]

    response = client.chat.completions.create(model=model,messages=messages, stream=stream)

    return response

def print_streaming_response(response):
    message = ""
    placeholder = st.empty()
    for chunk in response:
        delta = chunk.choices[0].delta
        if "content" in delta:
            message += delta["content"]
            placeholder.markdown(message + "|")
        else:
            break
    placeholder.markdown(message)
    return message



bible_text = "마태복음 5장"
keywords_1 = "축복"
keywords_2 = "가난"
keywords_3 = ""
sermon_title = "행복"

prompt_template = """
{bible_text}의 내용과 관련이 있는 설교제목과 설교주제를 만들어 주세요.
{sermon_title}과 관련이 있는 설교제목과 설교주제를 만들어 주세요.
설교제목을 만들 때는 반드시 하나님, 예수님, 성령님, 중의 하나가 들어가야 해요. 
설교주제는 10단어 이내에서 만들어 주세요. 
설교제목과 설교주제는 깊은 연관성이 있어야 해요. 
설교주제는 설교자의 주장이어야해요.
제목처럼 끝내지 말고, "~~ 한다"는 양식으로 만들어주세요. 
설교제목과 관련해서 참고할 만한 다른 성경구절들도 추천해 주세요. 
설교제목을 만들 때에 {keywords_1}, {keywords_2}, {keywords_2}를 참고해서 작성해 주세요. 
제목과 관련이 깊은 성경 구절도 알려주세요. 
성경구절 전체를 표시해 주세요. 
성경구절은 개신교 개역개정 성경으로 표시해 주세요.
3 개의 제목을 만들어 주세요.
아래의 예시와 같이 출력해주세요.

예시)
---
1.
설교 제목: "하나님의 행복의 비밀"

설교 주제: "하나님의 허락 아래에서 찾는 진정한 행복"

관련 성경: 시편 1장 1절 - 3절

(시 1:1) 복 있는 사람은 악인들의 꾀에 따르지 아니하며 죄인들의 길에 서지 아니하며 오만한 자들의 자리에 앉지 아니하며 (시 1:2) 오직 여호와의 율법을 즐거워하여 그 율법을 주야로 묵상하는 자라 (시 1:3) 그는 시냇가에 심은 나무가 때가 이르면 열매를 맺으며 그 잎사귀도 시들지 아니함 같으니 그의 하는 일이 다 형통하리로다

2.
설교 제목: "예수님으로 인한 진정한 행복"

설교 주제: "예수님과의 관계를 통해 영원한 행복을 얻는 방법"

관련 성경: 요한복음 15장 11절

(요 15:11) 이것을 내가 너희에게 말한 것은 나의 기쁨이 너희 안에 있어 너희의 기쁨이 충만하게 함이니라

3.
설교 제목: "성령님의 행복한 변화"

설교 주제: "성령님의 변화를 받아 진정한 행복을 누리는 삶"

관련 성경: 롬서서 14장 17절

(롬 14:17) 하나님의 나라는 먹고 마시는 것이 아니요 오직 의의 묵시고 평강과 성령 가운데 있는 기쁨이니라
---

""".strip()


# system_role = "당신은 매우 훌륭한 목회 도우미입니다."

############## 보여지는 화면 ############3
st.markdown("<h1 style='text-align: center; color: black;'>Chat Bot 인공지능 목회연구소</h1>", unsafe_allow_html=True)
# st.markdown("<h2 style='text-align: center; color: black;'>💖 저는 인공지능 목회 도우미입니다</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>👌 설교 제목과 주제, 성경 구절을 추천해 드립니다</h3>", unsafe_allow_html=True)

# # st.title("Chat Bot 인공지능 목회연구소")
# st.subheader("💖 저는 인공지능 목회 도우미입니다")
# st.markdown("👌 설교 제목과 주제, 성경 구절을 추천해 드립니다")
auto_complete = st.toggle("⚡ 예시로 채우기")

with st.form("form"):
    example = {
    "bible_text": "마태복음 5장",
    "keyword1": "축복",
    "keyword2": "가난",
    "keyword3": "",
    "sermon_title": "행복"
    }


    col1, col2 = st.columns(2)
    with col1:
        bible_text = st.text_input("성경 구절", value=example["bible_text"] if auto_complete else "")
    with col2:
        sermon_title = st.text_input("주제어", value=example["sermon_title"] if auto_complete else "")
        
    col1, col2, col3 = st.columns(3)
    with col1:
        keywords_1 = st.text_input(label="키워드 1", value=example["keyword1"] if auto_complete else "")
    with col2:
        keywords_2 = st.text_input(label="키워드 2", value=example["keyword2"] if auto_complete else "")
    with col3:
        keywords_3 = st.text_input(label="키워드 3", value=example["keyword3"] if auto_complete else "")
          
    submit = st.form_submit_button("확인")

    
if submit:

    prompt = prompt_template.format(bible_text=bible_text, keywords_1=keywords_1,keywords_2=keywords_3, keywords_3=keywords_3, sermon_title=sermon_title)
    
    system_role = "당신은 훌륭한 목회 도우미입니다. 아주 창의적이고 은혜로운 설교 제목을 만들수 있고, 설교 주제문을 아주 잘 만들수 있습니다."

    with st.spinner("설교제목과 주제를 생성 중입니다."):
        response = request_chat_completion(prompt=prompt, system_role=system_role, stream=True)
        

    print_streaming_response(response)

    st.write_stream(response)
        
        # st.session_state = (response.choices[0].message.content)
        
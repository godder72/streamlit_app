
from openai import OpenAI
import streamlit as st
from streamlit_option_menu import option_menu
import time
# import toml
import os


file_id = st.secrets['file']
assistant_id = st.secrets['assistant_id']
thread_id = st.secrets['thread_id']

client = OpenAI(api_key = st.secrets["key"])


def request_chat_completion(prompt,system_role="당신은 매우 훌륭한 목회 도우미입니다.",model="gpt-3.5-turbo",stream=True):

    messages = [{"role": "system", "content": system_role}, {"role": "user", "content": prompt}]

    response = client.chat.completions.create(model=model,messages=messages, stream=stream)

    return response

# response.choices[0].message.content

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

sermon_title = "사랑"
sermon_sentence = "하나님의 사랑은 아버지의 사랑과 비슷하다"
keyword_1 = "사랑"
keyword_2 = "아버지"
keyword_3 = ""

prompt_template = """

{sermon_title}이라는 주제로 설교문을 작성하려고 해. 
{sermon_sentence} 라는 주장을 하려고 해.
{keyword_1},{keyword_2},{keyword_3} 등의 키워드도 참고해서 위 주제와 관련된 예화를 찾아주세요.

예화를 5개 찾아주세요. 

첫째는 성경 이야기에서 찾아 주시고요. 
성경 이야기는 성경의 구절을 명확하게 알려줘. 
길이가 1000 단어 이상 되어야 해요. 
예화는 매우 구체적이어야 해요. 

둘째는 신앙도서에서 자료를 찾아줘.
영어가 원문인 자료는 영어 제목과 영어 저자 이름을 알려줘.
예화는 매우 구체적이어야 해요. 
길이가 1000 단어 이상 되어야 해요. 

셋째는 일반도서에서 그 자료를 찾아줘.
영어가 원문인 자료는 영어 제목과 영어 저자 이름을 알려줘.
예화는 매우 구체적이어야 해요. 
길이가 1000 단어 이상 되어야 해요. 

넷째는 통계 자료를 참고해서 관련 정보를 제공해 주세요. 
통계자료의 출처나 연도를 표시해줘.
예화는 매우 구체적이어야 해요. 
길이가 1000 단어 이상 되어야 해요. 

다섯째는 신문기사에서 그 자료를 찾아줘. 
신문명을 명확히 알려줘.
영어가 원문인 자료는 영어 제목과 영어 저자 이름을 알려줘.
예화는 매우 구체적이어야 해요. 
길이가 1000 단어 이상 되어야 해요. 

예시)
------
성경 이야기:

요한 3:16에는 하나님의 큰 사랑이 기록되어 있습니다. "하나님이 세상을 이처럼 사랑하사 독생자를 주셨으니 이는 그를 믿는 자마다 멸망하지 않고 영생을 얻게 하려 하심이니라." 이 구절은 하나님의 사랑이 아버지의 사랑과 같다는 것을 보여줍니다. 바로 그 눈에 희생하지 않는 자신의 유일한 아들을 내주셔서 우리를 구원하는 하나님의 사랑이란 말이지요.

신앙도서:

제목: "Impactful Love: God's Love for the Needy"

저자: 저자 알랜 스미스

"Impactful Love: God's Love for the Needy"라는 책은 신앙자가 신앙 생활에서 하나님의 사랑이 어떻게 가난한 자들과의 관계에서 나타날 수 있는지를 다루고 있습니다. 이 책은 저자 알랜 스미스의 생동감 있는 예화와 경험을 통해 하나님의 사랑이 가난한 자들의 필요를 충족시키는 방법을 설명합니다. 알랜 스미스는 자원봉사자로서 가난한 이웃들과 함께 일한 경험을 토대로, 하나님의 사랑이 어떻게 변화를 이루고 희망을 가져다 줄 수 있는지를 살펴봅니다. 예를 들면, 가난한 한 장애인의 이야기를 통해 그의 삶이 하나님의 사랑을 경험하고 기적적인 회복을 이루게 되었던 이야기 등이 소개되고 있습니다.

일반도서:

제목: "The Power of Kindness: Transforming Lives through Love"

저자: 제리 하워드

일반도서로는 "The Power of Kindness: Transforming Lives through Love"라는 책이 있습니다. 이 책은 제리 하워드의 저서로, 인간 관계에서 나타나는 사랑과 친절의 힘을 다룹니다. 제리 하워드는 매우 구체적인 예를 통해 사람들이 어떻게 애정과 관심을 통해 다른 사람을 돕고 변화시킬 수 있는지를 설명합니다. 특히, 하나님의 사랑과 영감을 받아 가난한 자들에게 친절하게 다가가서 변화를 이룰 수 있다는 사례가 다수 소개되고 있습니다. 이 책은 하나님의 사랑이 일상적인 대인관계에서 어떻게 실천될 수 있는지를 보여줍니다.

통계 자료:

유엔 세계식량계획(UN World Food Programme)의 2020년 보고서에 따르면, 세계적으로 약 8억 명의 사람이 식량 부족에 처해있습니다. 이는 전 세계 인구의 약 1/10에 해당하는 비율입니다. 특히, 아프리카와 아시아 지역에서는 식량 부족에 가장 많이 직면하고 있습니다. 이 통계는 가난한 사람들이 식량문제와 식품 부족으로 고통받고 있음을 보여줍니다. 하나님의 사랑으로부터 영감받아 국제기구와 다국적 단체들이 식량지원 및 농업 개발 프로젝트를 통해 이 문제를 해결하기 위해 노력하고 있습니다.

신문기사:

영국의 "The Guardian"에서 발행된 기사인 "Love in Action: Empowering the Poor Through Community Support"에는 지역 사회가 가난한 사람들을 돕고자 하는 여러 사례가 소개되었습니다. 이 기사에서는 자선단체, 지역 목회 단체, 지역 정부, 사업가 등 다양한 주체가 가난한 이웃들에게 직접적이고 지속적인 지원을 제공하는 방법을 설명하고 있습니다. 예를 들어, 한 지역 사회는 음식물 낭비를 줄이기 위한 캠페인을 진행하며, 다른 지역 사회는 직업 훈련과 고용 기회를 제공하여 가난한 사람들이 경제적으로 독립할 수 있도록 돕고 있습니다. 이 기사는 하나님의 사랑과 관련하여 지역 사회의 협력을 강조하며, 가난한 자들의 삶을 변화시키는 기반이 된 사회적 제도와 프로그램의 중요성을 다루고 있습니다. 장애인들의 성소수자들에게 적용되는 애정과 관심이 어떻게 변화를 일으키고 희망을 가져다주는지에 대한 재구성입니다. 아름답고 독창적인 이야기는 가난과 불평한 이웃들을 돕는 하나님의 사랑을 통해 어떻게 공유될 수 있는지를 보여줍니다.

이러한 도서와 자료들은 하나님의 사랑과 관련된 다양한 측면을 살펴보고, 우리의 사회와 세계에 적용하는 방법을 고려합니다. 하나님의 사랑을 통해 가난한 자를 돕고 사랑하는 방법은 우리가 일상에서 실천할 수 있는 중요한 메시지입니다.

더 많은 도움이나 자료가 필요하신 경우, 책이나 보고서, 신문기사 등에 대한 추가적인 분석이나 정보를 요청해 주시면 도와드리겠습니다. 감사합니다.
----


""".strip()


# system_role = "당신은 매우 훌륭한 목회 도우미입니다."

############## 보여지는 화면 ############3

st.title("🤖 Chat Bot 인공지능 목회연구소")
st.subheader("📰키워드를 입력하시면, 관련 예화를 찾아드립니다.")
auto_complete = st.toggle("⚡ 예시로 채우기")


with st.form("form"):

    example = {
    "sermon_title": "사랑",
    "sermon_sentence": "하나님의 사랑은 아버지의 사랑과 비슷하다",
    "keyword1": "사랑",
    "keyword2": "아버지",
    "keyword3": ""
    }
    col1, col2 = st.columns(2)
    with col1:
        sermon_title = st.text_input("주제", value=example["sermon_title"] if auto_complete else "")
    with col2:
        ""

    sermon_sentence = st.text_input("주제문을 자세히 입력해주세요.", value=example["sermon_sentence"] if auto_complete else "")
        
    col1, col2, col3 = st.columns(3)
    with col1:
        keywords_1 = st.text_input(label="키워드 1", value=example["keyword1"] if auto_complete else "")
    with col2:
        keywords_2 = st.text_input(label="키워드 2", value=example["keyword2"] if auto_complete else "")
    with col3:
        keywords_3 = st.text_input(label="키워드 3", value=example["keyword3"] if auto_complete else "")
          
    submit = st.form_submit_button("확인")

    
if submit:

    prompt = prompt_template.format(sermon_title=sermon_title, sermon_sentence=sermon_sentence, keyword_1=keyword_1, keyword_2=keyword_2, keyword_3=keyword_3)
    
    system_role = "당신은 훌륭한 목회 도우미입니다. 아주 창의적이고 은혜로운 설교 제목을 만들수 있습니다."

    with st.spinner("목회도우미가 예화를 찾고 있습니다."):
        response = request_chat_completion(prompt=prompt, system_role=system_role, stream=True)

    print_streaming_response(response)

    st.write_stream(response)
    # generated_text = (response.choices[0].message.content)
    # st.text(generated_text)
        
        # st.session_state = (response.choices[0].message.content)
        
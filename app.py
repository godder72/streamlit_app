from openai import OpenAI
import streamlit as st


st.set_page_config(page_title="Ministry Assistant")

# st.title("인공지능 목회연구소")
# st.subheader("💛 저는 인공지능 목회 도우미입니다.") 
# st.markdown("✝ 무엇을 도와드릴까요?")


st.markdown("<h1 style='text-align: center;'>Chat Bot 인공지능 목회연구소</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>저는 인공지능 목회 도우미입니다.💛</h2>", unsafe_allow_html=True)

st.divider()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.page_link("pages/1_😍설교 아이디어 도우미.py", label="설교 아이디어 도우미", icon="😍")
with col2:
    st.page_link("pages/2_😎예화 도우미.py", label="예화 도우미", icon="😎")
with col3:
    st.page_link("pages/3_💖무엇이든물어보세요.py", label="무엇이든물어보세요", icon="💖")
with col4:
    st.page_link("pages/4_😅SUPPORT.py", label="SUPPORT", icon="😅")

st.divider()

st.markdown("저는 전문 신학 서적 파일을 가지고 있으며, 이 파일에서 여러 정보를 발췌하여 제공해 드릴수 있습니다. 현재 마태복음 관련 주석 1000페이지를 가지고 있으며, 관련 파일들은 지속적으로 업데이트될 예정입니다.")
st.markdown("1. 설교 아이디어 도우미 페이지에서는 설교 제목과 설교 주제문, 관련 성구를 제공하고 있습니다. 성경 본문이나 원하시는 주제어를 입력하시면 설교 아이디어를 제공해 드립니다.")
st.markdown("2. 예화 도우미 페이지에서는 설교와 관련된 예화 찾기를 도와드립니다. 주제나 주제문, 키워드 등을 입력하시면, 관련 성경이야기, 신앙서적 추천, 통계 자료, 신문 기사 자료등을 제공해 드립니다.")
st.markdown("3. 무엇이든 물어보세요 페이지에서는 부족하다고 생각되는 정보를 자세히 검색해 볼수 있습니다. 추천된 책이나, 신문기사 등에 대해서 자세히 물어보실 수 있습니다.")


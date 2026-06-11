import streamlit as st

st.set_page_config(
    page_title="나와 닮은 동물 찾기",
    page_icon="🐾"
)

st.title("🐾 나와 닮은 동물 찾기")

st.write("""
안녕하세요! 😄

이 프로그램은 간단한 질문을 통해
나와 가장 닮은 동물을 찾아주는 프로그램입니다.

왼쪽 메뉴를 눌러 시작해보세요!
""")
import streamlit as st

st.title("🔍 나와 닮은 동물 찾기")

st.write("질문에 답하고 나와 가장 닮은 동물을 찾아보자! 🐾")

q1 = st.radio(
    "1️⃣ 친구들과 있을 때 나는?",
    ["분위기를 이끄는 편", "조용히 듣는 편", "장난을 많이 치는 편"]
)

q2 = st.radio(
    "2️⃣ 주말에 더 하고 싶은 것은?",
    ["밖에서 놀기", "집에서 쉬기", "새로운 취미 도전"]
)

q3 = st.radio(
    "3️⃣ 친구들이 나를 가장 많이 뭐라고 말할까?",
    ["리더 같다", "착하다", "재밌다"]
)

q4 = st.radio(
    "4️⃣ 학교에서 나는?",
    ["발표를 잘한다", "조용히 집중한다", "친구들과 잘 어울린다"]
)

if st.button("결과 보기 🐾"):

    if q1 == "분위기를 이끄는 편" or q3 == "리더 같다":
        animal = "🦁 사자"
        desc = "자신감이 넘치고 리더십이 강한 성격!"

    elif q2 == "집에서 쉬기" and q4 == "조용히 집중한다":
        animal = "🦉 부엉이"
        desc = "생각이 깊고 신중한 성격!"

    elif q1 == "장난을 많이 치는 편" or q3 == "재밌다":
        animal = "🦦 수달"
        desc = "밝고 장난기 많은 성격!"

    elif q3 == "착하다":
        animal = "🐶 강아지"
        desc = "친절하고 친구를 잘 챙기는 성격!"

    else:
        animal = "🐱 고양이"
        desc = "독립적이고 자기만의 매력이 있는 성격!"

    st.success(f"당신과 가장 닮은 동물은 {animal}")
    st.subheader(desc)

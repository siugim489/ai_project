import streamlit as st

st.set_page_config(
    page_title="나와 닮은 동물 찾기",
    page_icon="🐾"
)

st.title("🐾 나와 닮은 동물 찾기")

st.write("질문에 답하면 나와 닮은 동물을 알려드립니다!")

q1 = st.selectbox(
    "친구들은 나를 어떤 사람이라고 하나요?",
    ["리더 같다", "착하다", "재밌다", "조용하다"]
)

q2 = st.selectbox(
    "주말에는 무엇을 하고 싶나요?",
    ["밖에서 놀기", "집에서 쉬기", "새로운 취미"]
)

if st.button("결과 보기 🐾"):

    if q1 == "리더 같다":
        st.success("🦁 사자")
        st.write("리더십이 강하고 자신감이 넘쳐요!")

    elif q1 == "착하다":
        st.success("🐶 강아지")
        st.write("친절하고 친구를 잘 챙겨요!")

    elif q1 == "재밌다":
        st.success("🦦 수달")
        st.write("밝고 장난기 많은 성격이에요!")

    else:
        st.success("🦉 부엉이")
        st.write("신중하고 생각이 깊은 성격이에요!")

st.markdown("---")

st.subheader("📚 동물 설명")

animal = st.selectbox(
    "동물을 선택하세요",
    ["사자", "강아지", "수달", "부엉이"]
)

if animal == "사자":
    st.info("🦁 리더십이 강하고 용감해요.")

elif animal == "강아지":
    st.info("🐶 사교적이고 친절해요.")

elif animal == "수달":
    st.info("🦦 활발하고 긍정적이에요.")

elif animal == "부엉이":
    st.info("🦉 관찰력이 뛰어나고 신중해요.")

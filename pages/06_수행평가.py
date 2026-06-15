import streamlit as st

st.title("🐾 나와 닮은 동물 찾기")

st.write("질문에 답하고 결과를 확인해보세요!")

q1 = st.selectbox(
"친구들은 나를 어떤 사람이라고 하나요?",
["리더 같다", "착하다", "재밌다"]
)

q2 = st.selectbox(
"주말에 무엇을 하고 싶나요?",
["밖에서 놀기", "집에서 쉬기", "새로운 취미"]
)

if st.button("결과 보기"):

```
if q1 == "리더 같다":
    st.success("🦁 당신은 사자형!")
    st.write("리더십이 강하고 자신감이 넘쳐요.")

elif q1 == "착하다":
    st.success("🐶 당신은 강아지형!")
    st.write("친절하고 친구를 잘 챙겨요.")

elif q1 == "재밌다":
    st.success("🦦 당신은 수달형!")
    st.write("밝고 장난기가 많아요.")
```

st.markdown("---")

animal = st.selectbox(
"동물 설명 보기",
["사자", "강아지", "수달"]
)

if animal == "사자":
st.info("🦁 리더십이 강하고 용감해요.")

elif animal == "강아지":
st.info("🐶 사교적이고 친절해요.")

elif animal == "수달":
st.info("🦦 활발하고 긍정적이에요.")

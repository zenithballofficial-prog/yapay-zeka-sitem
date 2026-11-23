import streamlit as st
from groq import Groq

st.title("Benim Yapay Zekam")
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
SISTEM = {"role": "system", "content": "Sen yardımsever bir Türkçe asistansın."}

if "mesajlar" not in st.session_state:
    st.session_state.mesajlar = []

for m in st.session_state.mesajlar:
    with st.chat_message(m["role"]):
        st.write(m["content"])

soru = st.chat_input("Bir şey yaz...")
if soru:
    st.session_state.mesajlar.append({"role": "user", "content": soru})
    with st.chat_message("user"):
        st.write(soru)
    cevap = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[SISTEM] + st.session_state.mesajlar,
    )
    metin = cevap.choices[0].message.content
    st.session_state.mesajlar.append({"role": "assistant", "content": metin})
    with st.chat_message("assistant"):
        st.write(metin)

import streamlit as st

st.title("Hastane Yatış Süresi Tahmini")

st.write("Lütfen hasta bilgilerini girin:")

age = st.slider("Yaş", 0, 100, 30)
gender = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])
admission_type = st.selectbox("Kabul Türü", ["Acil", "Planlı", "Diğer"])

if st.button("Tahmin Et"):
    st.write("Model tahmini: 7 gün (örnek)")

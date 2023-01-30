import streamlit as st

st.title("Text summarizer")
input_text = st.text_area(label='Enter full text:', value="", height=250)
st.button("submit")
output_text = st.text_area(label='Summarized text:', value="", height=250)


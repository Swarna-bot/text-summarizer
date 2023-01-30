import streamlit as st
import openai
import os
from summarizer.functions import summarize

try:
    openai.api_key = os.getenv('OPENAPI_KEY')

    #initalize state variable
    if "summary" not in st.session_state:
        st.session_state["summary"] = ""

    st.title("Text summarizer")
    
    input_text = st.text_area(label='Enter full text:', value="", height=250)
    st.button("Submit", on_click=summarize, kwargs={"prompt":input_text},)

    output_text = st.text_area(label='Summarized text:', value=st.session_state["summary"], height=250)
except:
    st.write('There was an error=(')


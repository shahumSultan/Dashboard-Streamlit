import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

st.set_page_config(page_title="Dashboard", layout='wide', initial_sidebar_state='collapsed')

st.title("Analytics Dashboard")
with st.sidebar:
    uploaded_file = st.file_uploader("Upload CSV", type=['csv'])
  
# Check if a file was uploaded
if uploaded_file is not None:
   df = pd.read_csv(uploaded_file, encoding="Latin-1")
   st.write("Uploaded file:") 
   st.dataframe(df)


llm = OpenAI(api_token="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")
pandas_ai = PandasAI(llm)

question = st.text_input("Talk to Data")
if question:
        response = pandas_ai(df, question)
        st.write("Response:")
        st.write(response)




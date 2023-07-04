import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

st.set_page_config(page_title="Dashboard", layout='wide', initial_sidebar_state='collapsed')

st.title("Analytics Dashboard")
st.subheader("Talk to Data")
with st.sidebar:
    uploaded_file = st.file_uploader("Upload CSV", type=['csv'], accept_multiple_files=False ,key='talk')
  
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




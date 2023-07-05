import streamlit as st
import pandas as pd
from pandasai import PandasAI  
import os
from pandasai.llm.openai import OpenAI

dir_path = os.getcwd()
llm = OpenAI(api_token="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")
pandas_ai = PandasAI(llm, save_charts=True, save_charts_path=dir_path)

st.set_page_config(page_title="Dashboard", layout='wide', initial_sidebar_state='collapsed')

st.title("Analytics Dashboard")
with st.sidebar:
    st.header("Pages")
    st.title("CSV File Uploader")
    st.write("Please upload a CSV file.")
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='Latin-1')
    st.write(df)

question = st.text_input(label='Talk to Data')

if question is '':
    st.write("Nothing")
else:
    output = pandas_ai(df, question)
    st.write(output)
    if isinstance(question, str) and any(word in question.lower() for word in ["chart", "graph", "image","fig","figure","image","img"]):
        folder_path = "D:/pandasai/exports/charts/chart.png"
        image = open(folder_path, "rb").read()
        st.image(image, caption='Image Caption', use_column_width=True)
   
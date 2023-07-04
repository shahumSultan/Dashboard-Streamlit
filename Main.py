import streamlit as st

st.set_page_config(page_title="Dashboard", layout='wide', initial_sidebar_state='collapsed')

st.title("Analytics Dashboard")
st.subheader("Talk to Data using PandasAI")

with st.sidebar:
    st.header("Pages")
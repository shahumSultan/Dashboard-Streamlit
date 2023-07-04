import streamlit as st
import pandas as pd
from neuralprophet import NeuralProphet, set_log_level
    
st.set_page_config(page_title="Dashboard", layout='wide', initial_sidebar_state='collapsed')
set_log_level("ERROR")

def forNeuralProphet(dataframe):
    data = dataframe[['SALES']]
    data = data.rename(columns={'SALES':'y'})
    start_date = '2019-01-01'
    data['ds'] = pd.date_range(start=start_date, periods=len(data), freq='D')
    data = data[['ds', 'y']]
    
    model = NeuralProphet(
        n_changepoints=10,
        yearly_seasonality=True,
        weekly_seasonality=False,
        daily_seasonality=False,
        learning_rate=0.02
    )
    
    metrics = model.fit(data)
    data_future = model.make_future_dataframe(data, n_historic_predictions=True, periods=365)
    forecast = model.predict(data_future)
    graph = model.plot(forecast)
    
    return graph

st.title("Analytics Dashboard")
st.subheader("Sales Forecasting")

with st.sidebar:
    uploadedFile = st.file_uploader(label='Upload CSV', type=['csv'], accept_multiple_files=False)
    
if uploadedFile is not None:
    df = pd.read_csv(uploadedFile, encoding='Latin-1')
    st.write(df)
    
    st.plotly_chart(forNeuralProphet(df), theme='streamlit')
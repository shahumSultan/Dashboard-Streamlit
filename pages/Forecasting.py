import streamlit as st
import pandas as pd
from neuralprophet import NeuralProphet, set_log_level
    
st.set_page_config(page_title="Dashboard", layout='wide', initial_sidebar_state='expanded')
set_log_level("ERROR")

def forNeural(dataframe):
    data = dataframe[['SALES']]
    data = data.rename(columns={'SALES':'y'})
    startDate = '2020-01-01'
    data['ds'] = pd.date_range(start=startDate, periods=len(data), freq='D')
    data = data[['ds', 'y']]
    data = data.head(365)
    
    model = NeuralProphet(
        n_changepoints=10,
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=True,
        learning_rate=0.01
    )
    model.set_plotting_backend('plotly')
    metrics = model.fit(data)
    df_future = model.make_future_dataframe(data, n_historic_predictions=True, periods=365)
    forecast = model.predict(df_future)
    graph = model.plot(forecast)
    
    return graph
    

st.title("Analytics Dashboard")
st.subheader("Sales Forecasting")

with st.sidebar:
    uploadedFile = st.file_uploader(label='Upload CSV', type=['csv'], accept_multiple_files=False, key='sales')
  
if uploadedFile is not None:
    df = pd.read_csv(uploadedFile, encoding='Latin-1')
    data = forNeural(df)
    st.plotly_chart(data, use_container_width=True)
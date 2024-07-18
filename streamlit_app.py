import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.subheader('あなたの点数を入力してください')

ma = st.number_input('数学',value = 0,min_value=0,max_value=100)
sc = st.number_input('理科',value = 0,min_value=0,max_value=100)
ja = st.number_input('国語',value = 0,min_value=0,max_value=100)
en = st.number_input('英語',value = 0,min_value=0,max_value=100)
so = st.number_input('社会',value = 0,min_value=0,max_value=100)

data = go.Bar(
    x = ['数学','理科','国語','英語','社会'],
    y = [ma,sc,ja,en,so]
)
fig = go.Figure(
    data = data,
)

if st.button('結果を見る'):
    fig.show()
import streamlit as st
import pandas as pd
import plotly.graph_objs as go

st.subheader('あなたの点数を入力してください')

ma = st.number_input('数学',value = 0,label='number',min_value=0,max_value=100,placeholder = 'type your score')
sc = st.number_input('理科',varue = 0,label='number',min_value=0,max_value=100,placeholder = 'type your score')
ja = st.number_input('国語',varue = 0,label='number',min_value=0,max_value=100,placeholder = 'type your score')
en = st.number_input('英語',varue = 0,label='number',min_value=0,max_value=100,placeholder = 'type your score')
so = st.number_input('社会',varue = 0,label='number',min_value=0,max_value=100,placeholder = 'type your score')

sub = ['数学','理科','国語','英語','社会']
scores = [ma,sc,ja,en,so]

def gra():
    fig = go.Figure(data = [go.Bar(x=sub,y=scores)])
    fig.update_layout(
        xaxis = dict(
            tickangle = 0,
            title_text = '教科',
            title_standoff = 100
        ),
        yaxis = dict(
            tickangle = 0,
            title_text = '点数',
            title_standoff = 100
        ),
        title = 'テストの点数')

if st.button('結果を見る'):
    gra()
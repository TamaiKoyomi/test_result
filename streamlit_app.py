import streamlit as st
import pandas as pd
import plotly.graph_objs as go

st.subheader('あなたの点数を入力してください')

ma = st.number_input('数学',value = None,placeholder = 'type your score')
sc = st.number_input('理科',value = None,placeholder = 'type your score')
ja = st.number_input('国語',value = None,placeholder = 'type your score')
en = st.number_input('英語',value = None,placeholder = 'type your score')
so = st.number_input('社会',value = None,placeholder = 'type your score')

sub = ['数学','理科','国語','英語','社会']
scores = [ma,sc,ja,en,so]

def judge():
    if ma > 100 or ma < 0:
        st.write('数学の値が正しくありません。正しい値を入力してください。')
    if sc > 100 or sc < 0:
        st.write('理科の値が正しくありません。正しい値を入力してください。')
    if ja > 100 or ja < 0:
        st.write('国語の値が正しくありません。正しい値を入力してください。')
    if en > 100 or en < 0:
        st.write('英語の値が正しくありません。正しい値を入力してください。')
    if so > 100 or so < 0:
        st.write('社会の値が正しくありません。正しい値を入力してください。')

def gra():
    fig = go.Figure(data = [go.Bar(x = '教科',y = '点数')])
    fig.update_layout(
        xaxis = dict(
            tickangle = 0,
            title_text = '教科',
            title_standoff = 100
        )
        yaxis = dict(
            tickangle = 0,
            title_text = '点数',
            title_standoff = 100
        )
        title = 'テストの点数'
    )

if st.button('結果を見る'):
    if judge() == True:
        gra()
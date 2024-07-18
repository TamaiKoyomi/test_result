import streamlit as st

st.subheader('あなたの点数を入力してください')

ma = st.number_input('数学',value = None,placeholder = 'type your score')
sc = st.number_input('理科',value = None,placeholder = 'type your score')
ja = st.number_input('国語',value = None,placeholder = 'type your score')
en = st.number_input('英語',value = None,placeholder = 'type your score')
so = st.number_input('社会',value = None,placeholder = 'type your score')
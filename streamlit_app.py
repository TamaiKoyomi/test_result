import streamlit as st

st.subheader('あなたの点数を入力してください')

ma = round(st.number_input('数学'))
sc = round(st.number_input('理科'))
ja = round(st.number_input('国語'))
en = round(st.number_input('英語'))
so = round(st.number_input('社会'))
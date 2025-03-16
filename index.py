from os import path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')

df_customer = pd.read_csv(path.join('datasets', 'customer reviews.csv'))
df_top100 = pd.read_csv(path.join('datasets', 'Top-100 Trending Books.csv'))

price_max = df_top100['book price'].max()
price_min = df_top100['book price'].min()

max_price = st.sidebar.slider("Price range", price_min, price_max, price_max)

df_books = df_top100[df_top100['book price'] <= max_price]
df_books

col1, col2 = st.columns(2)
fig1 = px.bar(df_books['year of publication'].value_counts())
fig2 = px.histogram(df_books['book price'])
col1.plotly_chart(fig1)
col2.plotly_chart(fig2)

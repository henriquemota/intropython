from os import path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')

df_customer = pd.read_csv(path.join('datasets', 'customer reviews.csv'))
df_top100 = pd.read_csv(path.join('datasets', 'Top-100 Trending Books.csv'))

books = df_top100['book title'].unique()
book = st.sidebar.selectbox('Books', books)

df_books = df_top100[df_top100['book title'] == book]
df_reviews = df_customer[df_customer['book name'] == book]

book

df_books

df_reviews
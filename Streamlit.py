import streamlit as st
import pandas as pd
import numpy as np

xls = st.file_uploader("Escolha um arquivo:", type="xlsx")
df1 = pd.read_excel(xls)
print (df1)


df1.head()
df1list = ['Coluna1','Coluna2']
df1['results'] = df1[list].sum(axis=1)
print(df1)

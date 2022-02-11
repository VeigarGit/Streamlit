import streamlit as st
import pandas as pd
import numpy as np

df1 = st.file_uploader("Escolha um arquivo:", type="xlsx")
df = pd.read_excel(df1)

if df1:
  st.dataframe(df1)



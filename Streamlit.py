import streamlit as st
import pandas as pd
import numpy as np

xls = pd.ExcelFile(r'https://docs.google.com/spreadsheets/d/11-inHHG35pbGF3WyDZPBMPRcXVQoEGfkFt5RhxbBLQM/edit?usp=sharing')
df1 = pd.read_excel(xls, 'Página1')
df2 = pd.DataFrame.to_excel(xls, 'Página2')
print (df1)
print (df2)

df1.head()
df1list = ['Coluna1','Coluna2']
df1['results'] = df1[list].sum(axis=1)
print(df1)

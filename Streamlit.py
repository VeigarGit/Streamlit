import streamlit as st
import pandas as pd
import numpy as np

xls = pd.ExcelFile(r'C:\Users\Rafael\Desktop\python\Streamlit\Streamlit\Streamlit\Somatoria.xlsx')
df1 = pd.read_excel(xls)
print (df1)


df1.head()
df1list = ['Coluna1','Coluna2']
df1['results'] = df1[list].sum(axis=1)
print(df1)

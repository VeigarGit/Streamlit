import streamlit as st
import pandas as pd
import numpy as np

xls = pd.ExcelFile(r'https://github.com/VeigarGit/Streamlit/blob/2f470b6a954fed676cec9d02c2b4afafc30c60bc/Somatoria.xlsx')
df1 = pd.read_excel(xls, 'Plan1')
df2 = pd.DataFrame.to_excel(xls, 'Plan2')
print (df1)
print (df2)

df1.head()
df1list = ['Coluna1','Coluna2']
df1['results'] = df1[list].sum(axis=1)
print(df1)

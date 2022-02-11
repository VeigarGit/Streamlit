import streamlit as st
import pandas as pd
import numpy as np

df1 = pd.read_execel(r'Somatoria.xlsx')

print (df1)


df1.head()
df1list = ['Coluna1','Coluna2']
df1['results'] = df1[list].sum(axis=1)
print(df1)

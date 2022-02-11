import streamlit as st
import pandas as pd
import numpy as np

xls = st.file_uploader("Escolha um arquivo:", type="xlsx")

xlslist= ['Coluna1','Coluna2']
xls['results'] = xlslist[list].sum(axis=1)
print(xls)

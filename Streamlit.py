import streamlit as st
import pandas as pd
import openpyxl
lista_soma = list()
arquivo = st.file_uploader("Escolha um arquivo:", type="xlsx")

if arquivo:
    df = pd.read_excel(arquivo)
    st.dataframe(df)

    for i in range(0, len(df)):
        lista_soma.append(df['COLUNA 1'][i]+df['COLUNA 2'][i])

    df_soma = pd.DataFrame(lista_soma, columns = ["SOMA"])
    st.table(df_soma)

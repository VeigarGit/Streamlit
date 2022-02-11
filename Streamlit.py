import streamlit as st
import pandas as pd
st.title("execute app")

df = pd.read_csv("Somatoria.xlxx")
st.table(df)

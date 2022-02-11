import streamlit as st
import pandas as pd

st.write("My First Streamlit Web App")

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6]})
df_result = df.groupby(["one","two"]).sum().reset_index()
st.write(df)

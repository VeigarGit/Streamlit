import streamlit as st
import pandas as pd

st.title("Connect to Google Sheets")
x = "https://docs.google.com/spreadsheets/d/11-inHHG35pbGF3WyDZPBMPRcXVQoEGfkFt5RhxbBLQM/edit?usp=sharing"
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(x)

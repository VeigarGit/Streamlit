import Streamlit as st
from gsheetsdb import connect

# .streamlit/secrets.toml

public_gsheets_url = "https://docs.google.com/spreadsheets/d/11-inHHG35pbGF3WyDZPBMPRcXVQoEGfkFt5RhxbBLQM/edit?usp=sharing"


# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(tll=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

sheet_url = st.secrets["https://docs.google.com/spreadsheets/d/11-inHHG35pbGF3WyDZPBMPRcXVQoEGfkFt5RhxbBLQM/edit?usp=sharing"]
rows = run_query(f'SELECT * FROM "{https://docs.google.com/spreadsheets/d/11-inHHG35pbGF3WyDZPBMPRcXVQoEGfkFt5RhxbBLQM/edit?usp=sharing}"')

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")
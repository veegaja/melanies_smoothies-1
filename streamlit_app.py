# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

conn = st.connection("snowflake")
df = conn.query("select * from orders")
st.dataframe(df)




import streamlit as st
import pandas as pd
from venmo import get_all_transactions


st.title("All Transactions")
data = [t.to_df() for t in get_all_transactions()]
df = pd.DataFrame(data)  # Ensure this is a DataFrame, not a list

st.dataframe(df, height=500, use_container_width=True)
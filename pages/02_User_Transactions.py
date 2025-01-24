import pandas as pd
import streamlit as st
import venmo as v

st.title("User Transaction Data")

options = v.get_all_names_not_lower()
selected_option = st.multiselect("Choose one or more names", options)

for person in selected_option:
    st.write("## " + person)
    for data in v.get_all_data_name(person):
        st.markdown(data)
    transactions = [t.to_df() for t in v.get_all_transactions_name(person)]
    df = pd.DataFrame(transactions)
    st.dataframe(df, use_container_width=True)

if not selected_option:
    st.warning("No Users Selected")
import streamlit as st
import venmo as v
import pandas as pd

st.title("All Data")
for data in v.get_all_data():
    st.markdown(f"### {data}")
st.markdown(f"### Total People Ever Sent or Received: {len(v.get_all_names())}")

x = 10
top_sent = v.get_topX_sent(x)
top_received = v.get_topX_received(x)
top_sent_and_received = v.get_topX_sent_and_received(x)


df1 = pd.DataFrame(top_sent, columns=["Name", "Amount ($)"])
df2 = pd.DataFrame(top_received, columns=["Name", "Amount ($)"])
df3 = pd.DataFrame(top_sent_and_received, columns=["Name", "Amount ($)"])
df1 = df1.style.format({"Amount ($)": "{:.2f}"})
df2 = df2.style.format({"Amount ($)": "{:.2f}"})
df3 = df3.style.format({"Amount ($)": "{:.2f}"})




col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Total Sent")
    st.table(df1)

with col2:
    st.subheader("Total Received")
    st.table(df2)

with col3:
    st.subheader("Sent & Received")
    st.table(df3)

top_amounts = v.all_amounts()
sorted_amounts = sorted(top_amounts.items(), key=lambda x: x[1], reverse=True)
sorted_amounts = sorted_amounts[:x]
sorted_amounts = [[round(list(x)[0])] + list(x)[1:] for x in sorted_amounts]

top_sent_and_received_freq = v.get_topX_sent_and_received_freq(x)
top_sent_and_received_freq = [[list(x)[0]] + [int(list(x)[1])] for x in top_sent_and_received_freq]


df4 = pd.DataFrame(sorted_amounts, columns=["Amount ($)", "Frequency "])
df5= pd.DataFrame(top_sent_and_received_freq, columns=["Name", "Frequency"])

st.subheader("Payment Frequencies")
new_col1, new_col2, = st.columns(2)
with new_col1:
    st.table(df4)

with new_col2:
    st.table(df5)

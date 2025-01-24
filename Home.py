import streamlit as st


st.set_page_config(
    page_title="Main Page",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.image("Venmo_logo.png", use_container_width=True)

st.markdown('''
### Discover insights and trends from your Venmo transactions with this interactive dashboard. 
## Here's what you can do:
    - See all transactions
    - See transaction history between specific users
    - see overall data
    - Explore a cool keyboard mashing algorithm
### Click on the sidebar links to start exploring!
'''
)





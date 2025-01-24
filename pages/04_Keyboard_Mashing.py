import streamlit as st
import pandas as pd
from venmo import ALL_TRANSACTIONS
from keyboard_mashing import keyboard_mashing_probability

all_note_probs = set()
for trans in ALL_TRANSACTIONS:
    all_note_probs.add((trans.note, keyboard_mashing_probability(trans.note)))
all_note_probs = sorted(list(all_note_probs), key=lambda x: x[1], reverse=True)


df = pd.DataFrame(all_note_probs,columns=["Note", "Keyboard Mashing Probability"])
st.title("Keyboard Mashing Algorithm")
st.dataframe(df, height=500, use_container_width=True)


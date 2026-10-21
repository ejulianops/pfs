import streamlit as st
import pandas as pd

st.title("Admin: Update Store Data")

# --- Password gate ---
if "admin_authenticated" not in st.session_state:
    st.session_state.admin_authenticated = False

if not st.session_state.admin_authenticated:
    pwd = st.text_input("Enter admin password", type="password")
    if st.button("Log in"):
        if pwd == st.secrets["admin_password"]:
            st.session_state.admin_authenticated = True
            st.rerun()
        else:
            st.error("Wrong password")
    st.stop()  # Don't show the editor until logged in

# --- Editable table ---
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    st.error("data.csv not found")
    st.stop()

edited_df = st.data_editor(df, hide_index=True, use_container_width=True)

# --- Save button ---
if st.button("💾 Save changes to data.csv"):
    edited_df.to_csv("data.csv", index=False)
    st.success("Saved! The public page will show the new data on next reload.")

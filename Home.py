import pandas as pd
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Plants", layout="wide")
st.title("Plant Fact Sheet")

# 1. Load the data first
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    st.error("❌ data.csv file not found in the current directory")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# 2. Search filter (operates on the loaded df)
q = st.text_input("Search client / site")
if q:
    df = df[
        df["client"].str.contains(q, case=False, na=False)
        | df["site name"].str.contains(q, case=False, na=False)
    ]

# 3. Display once, with the filtered (or full) data
st.dataframe(df, hide_index=True, use_container_width=True)

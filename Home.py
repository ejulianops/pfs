import pandas as pd
import streamlit as st

st.set_page_config(page_title="Plants", layout="wide")
st.title("Plant Fact Sheet")

try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    st.error("❌ data.csv file not found in the current directory")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

st.dataframe(df, hide_index=True, use_container_width=True)

st.download_button(
    label="⬇️ Download CSV",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="plant_fact_sheet.csv",
    mime="text/csv",
)

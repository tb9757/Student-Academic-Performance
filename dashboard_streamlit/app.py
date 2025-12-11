import streamlit as st
import pandas as pd
import numpy as np

#print(st.__version__)

st.title("Student Academic Performance")
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("This is fixed-width text.")
# st.markdown("**This text is bold using Markdown!**")

df = pd.read_csv('../data/academic_performance_cleaned.csv')
if st.button('View Data'):
    st.dataframe(df.head())
import streamlit as st
import pandas as pd
import numpy as np

#print(st.__version__)

def page1_body():
    """
    This function displays the content of Page one.
    """
    
    st.write('Dashboard for Student academic performance')
    df = pd.read_csv('../data/academic_performance_cleaned.csv')
    if "show_table" not in st.session_state:
        st.session_state.show_table = False
    if st.button('View Data'):
        st.session_state.show_table = not st.session_state.show_table
    if st.session_state.show_table:
        st.dataframe(df.head())


# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("This is fixed-width text.")
# st.markdown("**This text is bold using Markdown!**")
import streamlit as st
import pandas as pd
import numpy as np

def page1_body():
    """
    This function displays the content of Page one.
    """
    df = pd.read_csv('../data/academic_performance_cleaned.csv')
    col1, col2, col3, col4, col5 = st.columns(5)
    st.metric('Pupils', len(df))
    st.markdown('This is a synthetic dataset containing student '
                'academic metrics for 2000 individual pupils. The dataset '
                'includes attendance, internal exam scores, assignment '
                'performance, daily study habits, and final exam marks.')  
    if "show_table" not in st.session_state:
        st.session_state.show_table = False
    if st.button('View Data'):
        st.session_state.show_table = not st.session_state.show_table
    if st.session_state.show_table:
        st.dataframe(df.head())

    st.markdown('Two extra columns have been added, one is the mean average of '
                'the two internal test scores. '
                'The other has split pupils into two groups: ')
    st.markdown('- **High study group** > 3 hours study per day\n- **Low study group** ≤ 3 hours study per day')           
                

# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("This is fixed-width text.")
# st.markdown("**This text is bold using Markdown!**")

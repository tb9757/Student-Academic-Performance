import streamlit as st
import pandas as pd
# import numpy as np


def page1_body():
    """
    This function displays the content of Page one.
    """
    df = pd.read_csv('../data/academic_performance_cleaned.csv')
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric('Pupils', len(df))
    col2.metric('Mean Final Score (%)', df['Final Exam Marks (out of 100)'].mean().round(1))
    col3.metric('Mean Attendance (%)', df['Attendance (%)'].mean().round(1))
    col4.metric('Mean Test Score (%)', (df['Average Test Score'].mean()*2.5).round(1))
    col5.metric('Median study hours', df['Daily Study Hours'].median())
    st.markdown('This is a synthetic dataset containing student '
                'academic metrics for 2000 individual pupils. The dataset '
                'includes attendance, internal test scores, assignment '
                'performance, daily study habits, and final exam marks. '
                'Click below to view data, use the slider in the sidebar'
                'to chage the number of rows displayed')
    if "show_table" not in st.session_state:
        st.session_state.show_table = False
    if st.button('View Data'):
        st.session_state.show_table = not st.session_state.show_table
    if st.session_state.show_table:
        rows = st.sidebar.slider('No. of rows', 5, 50, step=5)
        st.dataframe(df.head(rows))

    st.markdown('Two extra columns have been added, one is the mean of '
                'the two internal test scores. '
                'The other has split pupils into two groups: ')
    st.markdown('- **High study group** > 3 hours study per day\n- **Low '
                'study group** ≤ 3 hours study per day')
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("This is fixed-width text.")
# st.markdown("**This text is bold using Markdown!**")

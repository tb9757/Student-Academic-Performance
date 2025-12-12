import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import seaborn as sns
import streamlit as st
sns.set_style('whitegrid')


def page1_body():
    """
    This function displays the content of Page one.
    """
    # df = pd.read_csv('../data/academic_performance_cleaned.csv')
    BASE_DIR = Path(__file__).resolve().parents[2]
    DATA_PATH = BASE_DIR / "data" / "academic_performance_cleaned.csv"

    df = pd.read_csv(DATA_PATH)

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric('Pupils', len(df))
    col2.metric('Mean Final Score (%)',
                df['Final Exam Marks (out of 100)'].mean().round(1))
    col3.metric('Mean Attendance (%)', df['Attendance (%)'].mean().round(1))
    col4.metric('Mean Test Score (%)',
                (df['Average Test Score'].mean()*2.5).round(1))
    col5.metric('Median study hours', df['Daily Study Hours'].median())
    st.markdown('This is a synthetic dataset containing student '
                'academic metrics for 2000 individual pupils. The dataset '
                'includes attendance, internal test scores, assignment '
                'performance, daily study habits, and final exam marks.'
                )
    st.markdown('Click to view data, use the slider and select '
                'columns to change display '
                )
    st.subheader("Explore the data")
    if "show_table" not in st.session_state:
        st.session_state.show_table = False
    if st.button('View Data'):
        st.session_state.show_table = not st.session_state.show_table
    if st.session_state.show_table:
        rows = st.sidebar.slider('No. of rows', 5, 50, step=5)
        cols = st.sidebar.multiselect("Select columns:", df.columns)
        if cols:
            st.dataframe(df[cols].head(rows))
        else:
            st.dataframe(df.head(rows))

    st.markdown('Two new columns have been added, one is the mean of '
                'the two internal test scores. '
                'The other has split pupils into two groups: ')
    st.markdown('- **High study group** > 3 hours study per day\n- **Low '
                'study group** ≤ 3 hours study per day')
    st.markdown('These new columns are used later in the hypothesis '
                'testing pages (particularly Hypotheses 1, 2, and 3).')
    with st.sidebar.expander("Explore numerical distributions",
                             expanded=False):
        # store numerical column names in a list called num_cols
        num_cols = df.select_dtypes(['int64', 'float64']).columns
        st.radio('Show Distribution for:',
                 num_cols, key='dist_col')  # saving choice in session state
    if 'dist_col' in st.session_state:
        col = st.session_state['dist_col']
        st.subheader(f'{col} distribution')
        st.write('Select distribution with expander in sidebar')
        plt.figure(figsize=(8, 4))
        sns.histplot(data=df, x=col, kde=True, bins=20)
        plt.title(f'{col} distribution')
        st.pyplot(plt.gcf())   # Show plot in Streamlit gcf - get current fig
        plt.clf()              # Reset matplotlib

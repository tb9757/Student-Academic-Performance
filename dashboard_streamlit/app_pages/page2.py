import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
import plotly.express as px
import seaborn as sns
import streamlit as st


def page2_body():
    """
    This function displays the content of Page one.
    """
    BASE_DIR = Path(__file__).resolve().parents[2]
    DATA_PATH = BASE_DIR / "data" / "academic_performance_cleaned.csv"
    df = pd.read_csv(DATA_PATH)
    st.header('Hypothesis 1:')
    st.subheader('Average internal test score is more strongly correlated '
                 'with final exam mark than attendance.')
    st.markdown('This hypothesis compares importance of being '
                'consistently in school versus performing well in '
                'internal assessments. It is comparing engagement '
                'and consistency with academic ability and prior '
                'knowledge.')
    st.markdown('Correlation coefficients are compared for:')
    st.markdown('- Attendance and final test scores.\n - Average internal '
                'test scores and final test scores.')

    tab1, tab2 = st.tabs(['Average Test Score vs Final Exam Mark',
                          'Attendance vs Final Exam Mark'])

    with tab1:
        st.subheader('Average Test Score vs Final Exam Mark')
        fig = px.scatter(df, x='Average Test Score',
                         y='Final Exam Marks (out of 100)',
                         trendline='ols')
        st.plotly_chart(fig)
    with tab2:
        st.subheader('Attendance vs Final Exam Mark')
        fig2 = px.scatter(df, x='Attendance (%)',
                          y='Final Exam Marks (out of 100)',
                          trendline='ols')
        st.plotly_chart(fig2)
    st.subheader('Correlation')

    # Select the columns that I want assess correlation
    corr_cols = ['Attendance (%)', 'Assignment Score (out of 10)',
                 'Daily Study Hours', 'Final Exam Marks (out of 100)',
                 'Average Test Score']
    # calculate pearson correlation coefficient for these columns
    df_corr = df[corr_cols].corr(method='spearman')
    st.table(df_corr)

    # code copied from LMS to remove duplicated side
    fig, ax = plt.subplots()
    mask = np.zeros_like(df_corr)
    mask[np.triu_indices_from(mask)] = True
    sns.heatmap(
        df_corr,
        annot=True,
        mask=mask,
        cmap='coolwarm',
        annot_kws={"size": 8},
        linewidths=0.5,
        ax=ax
        )
    ax.set_ylim(df_corr.shape[1], 0)
    st.pyplot(fig)

    st.subheader("Conclusion for Hypothesis 1")
    st.markdown("""Average internal test score shows a much stronger
    positive relationship with final exam marks than attendance.
    Both the scatter plots and the correlation heatmap confirm
    this: test scores are far more closely aligned with final
    exam performance, while attendance shows only a weak
    association.""")

    st.success("Hypothesis 1 is supported — prior academic performance is a "
               "stronger predictor of final exam outcomes than attendance.")

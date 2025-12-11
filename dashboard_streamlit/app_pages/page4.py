import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


def page4_body():
    """
    This function displays the content of Page four.
    """
    st.header('Hypothesis 3:')
    st.subheader("Students studying for more than 3 hours per day "
                 "have significantly higher final exam marks than "
                 "those who study 3 hours or fewer.")
    df = pd.read_csv('../data/academic_performance_cleaned.csv')

    st.markdown("")
    df_pivot = pd.pivot(df.drop(columns=['Attendance (%)',
                                         'Internal Test 1 (out of 40)',
                                         'Internal Test 2 (out of 40)',
                                         'Assignment Score (out of 10)',
                                         'Daily Study Hours',
                                         'Average Test Score']),
                        columns='Study Group',
                        values='Final Exam Marks (out of 100)')

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
    sns.histplot(data=df_pivot, kde=True, bins=20, ax=axes[0], )
    for col in df_pivot.columns:
        axes[0].axvline(df_pivot[col].mean(),
                        color='r',
                        linestyle='dashed',
                        linewidth=1)
    sns.boxplot(data=df_pivot, ax=axes[1])
    axes[0].set(xlabel='Final Exam Score')
    st.pyplot(fig)
    st.markdown("""The dotted line on the
                histogram represents the mean, and the centre of the
                boxplot represents the median. These look **higher for
                blue group (high study hours)** in both cases.
                Visually it seems that the high study hours group
                achieved a higher final mark.
                """)
    st.markdown("""This can be tested statistically, in this case by 
                using the Mann-Whitney U test. This test was chosen
                due to the lack of normalality in these data. This test can
                tell us if the groups are statistically different.
                """)
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import pingouin as pg
import seaborn as sns
import streamlit as st


def page4_body():
    """
    This function displays the content of Page four.
    """
    BASE_DIR = Path(__file__).resolve().parents[2]
    DATA_PATH = BASE_DIR / "data" / "academic_performance_cleaned.csv"
    df = pd.read_csv(DATA_PATH)
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
                due to the lack of normality in these data. This test can
                tell us if the groups are statistically different.
                """)
    # Run the Mann–Whitney U test
    mwu_results = pg.mwu(x=df_pivot['high'], y=df_pivot['low'])

    u_val = mwu_results['U-val'].iloc[0]
    p_val = mwu_results['p-val'].iloc[0]
    rbc = mwu_results['RBC'].iloc[0]
    cles = mwu_results['CLES'].iloc[0]

    st.subheader("Hypothesis 3: Study Hours and Final Exam Marks")

    with st.container():
        st.markdown(
            "Comparing **> 3 hours/day** vs **≤ 3 hours/day** using a "
            "*Mann-Whitney U test*."
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("U statistic", f"{u_val:,.1f}")
        col2.metric("p-value", f"{p_val:.2e}")
        col3.metric("RBC (effect size)", f"{rbc:.3f}")
        col4.metric("CLES", f"{cles:.1%}")

        st.success(
            "Students who study **more than 3 hours per day** tend to achieve "
            "higher final exam marks. The difference between the two groups "
            "is **statistically significant** because p value is less than "
            "0.05 Students who study >3 hours/day score higher about 76% of "
            "the time compared to those studying ≤3 hours/day."
            )

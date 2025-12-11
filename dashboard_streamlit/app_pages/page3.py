import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st


def page3_body():
    """
    This function displays the content of Page one.
    """
    st.header('Hypothesis 2:')
    st.subheader('Average internal test scores explain more variance in '
                 'final exam marks than engagement based behaviours, such '
                 'as attendance, assignment score, and daily study hours.')
    df = pd.read_csv('../data/academic_performance_cleaned.csv')

    st.markdown("This hypothesis can be tested by fitting a linear regression "
                "model. The model's coefficients will be examined to see which "
                "variables contribute most to predicting final exam marks. The "
                "size of the coefficients will be compared for the engagement"
                "related metrics and the prior attainment metrics.")
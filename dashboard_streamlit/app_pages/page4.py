import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st


def page4_body():
    """
    This function displays the content of Page four.
    """
    st.header('Hypothesis 3:')
    st.subheader()
    df = pd.read_csv('../data/academic_performance_cleaned.csv')

    st.markdown()
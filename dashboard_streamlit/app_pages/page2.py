import streamlit as st
import pandas as pd
import plotly.express as px
def page2_body():
    """
    This function displays the content of Page one.
    """
    # df = pd.read_csv('../data/penguins_cleaned.csv')
    # choose_plot = st.radio('Choose Plot:', ['Bill length vs Bill depth', 'Bill Depth vs Body Mass'])
    # color = st.radio('Color by:', ['Species', 'Diet'])
    # if choose_plot == 'Bill length vs Bill depth':
    #     if color == 'Species':
    #         st.scatter_chart(data=df, x='bill_length_mm', y='bill_depth_mm', x_label='Bill Length (mm)', y_label='bill depth (mm)', color='species')
    #     elif color == 'Diet':
    #         st.scatter_chart(data=df, x='bill_length_mm', y='bill_depth_mm', x_label='Bill Length (mm)', y_label='bill depth (mm)', color='diet')
    # elif choose_plot == 'Bill Depth vs Body Mass':
    #     if color == 'Species':
    #         st.scatter_chart(data=df, x='body_mass_g', y='bill_depth_mm', x_label='Body mass (G)', y_label='bill depth (mm)', color='species')
    #     elif color == 'Diet':
    #         st.scatter_chart(data=df, x='body_mass_g', y='bill_depth_mm', x_label='Body mass (G)', y_label='bill depth (mm)', color='diet')

    # fig = px.scatter(df, x='bill_length_mm', y='bill_depth_mm', color='species', size='body_mass_g', hover_data=['island', 'sex'])
    # title='Penguin Species Clustering by Bill Dimensions'
    # fig.show()
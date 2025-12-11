import streamlit as st
import pandas as pd
import plotly.express as px


def page2_body():
    """
    This function displays the content of Page one.
    """
    st.header('Hypothesis 1:')
    st.subheader('Average internal test score is more strongly correlated with '
                'final exam mark than attendance.')
    df = pd.read_csv('../data/academic_performance_cleaned.csv')

    st.markdown('This hypothesis compares importance of being '
                'consistently in school versus performing well in '
                'internal assessments. It is comparing engagement '
                'and consistency with academic ability and prior '
                'knowledge.')
    st.markdown('Correlation coefficients are compared for:')
    st.markdown('- Attendance and final test scores.\n - Average internal '
                'test scores and final test scores.')

    tab1, tab2 = st.tabs(['Average Test Score vs Final Exam Mark', 'Attendance vs Final Exam Mark'])

    with tab1:
        st.subheader('Average Test Score vs Final Exam Mark')
        fig = px.scatter(df, x='Average Test Score', y='Final Exam Marks (out of 100)', trendline='ols')
        st.plotly_chart(fig)
    with tab2:
        st.subheader('Attendance vs Final Exam Mark')
        fig2 = px.scatter(df, x='Attendance (%)', y='Final Exam Marks (out of 100)', trendline='ols')
        st.plotly_chart(fig2)

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
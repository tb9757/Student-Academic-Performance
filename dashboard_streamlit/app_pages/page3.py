import pandas as pd
import plotly.express as px
import streamlit as st


def page3_body():
    """
    This function displays the content of Page one.
    """
    st.header('Hypothesis 2:')
    st.subheader('Average internal test scores explain more variance in '
                 'final exam marks than engagement based behaviours, such '
                 'as attendance, assignment score, and daily study hours.')
    # df = pd.read_csv('../data/academic_performance_cleaned.csv')

    st.markdown("""To test this hypothesis I used two linear regression models.
                Model 1 used only Average Test Score to predict Final Exam
                Marks. Model 2 included the engagement behaviours as
                additional predictors By comparing R² and RMSE across the
                two models, and examining the coefficients in Model 2, I
                can assess whether prior attainment explains more variance
                than engagement behaviours.""")
    model1_r2 = 0.73
    model1_RMSE = 5.6

    model2_r2 = 0.83
    model2_RMSE = 4.48

    coefficients = {
        "Attendance (%)": 2.9,
        "Assignment Score": 1.5,
        "Daily Study Hours": 1.8,
        "Average Test Score": 6.6
        }
    df_coef = pd.DataFrame({
        "Feature": coefficients.keys(),
        "Coefficient": coefficients.values()
    })
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Model 1 R²:", model1_r2)
    col2.metric("Model 2 R²:", model2_r2)
    col3.metric("Model 1 RMSE:", model1_RMSE)
    col4.metric("Model 2 RMSE:", model2_RMSE)

    fig = px.bar(df_coef, x='Feature', y='Coefficient',
                 title='Model 2 Coefficient Sizes')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
                ### Interpretation
Two regression models were fitted to evaluate the hypothesis:

- **Model 1** used only **Average Test Score** to predict final exam marks.
- **Model 2** included all **engagement behaviours** (attendance, assignment
score, daily study hours) *plus* Average Test Score.

**R²** shows how much of the variance in final exam marks each model explains.
Model 1 already explains a large amount of the variance, and adding engagement
behaviours in Model 2 increases R² further. This indicates that engagement
contributes something extra, but not as strongly as prior academic performance.

The bar chart shows the **relative size of the coefficients** in Model 2.
A larger coefficient means a stronger influence on the prediction.
Average Test Score has the largest coefficient by a wide margin, demonstrating
that it is the most important predictor of final exam marks.
        """)
    st.success("**Overall, these results support the hypothesis** that prior "
               "academic performance explains more variance in final exam "
               "outcomes than engagement-based behaviours.")

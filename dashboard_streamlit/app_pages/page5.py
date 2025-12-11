import streamlit as st


def page5_body():
    """
    This function displays the content of Page five.
    """
    st.header('Hypothesis 4:')
    st.subheader('A regression model that includes preprocessing steps will '
                 'perform better than a model trained on the raw data')

    st.markdown("""Preprocessing steps are steps taken to prepare
                the dataset so that the model can effectively learn.
                In this example the preprocessing step taken was feature
                scaling.
                """)
    st.markdown("""Feature scaling puts all of the number on a similar scale.
                This prevents features whose numbers are large
                disproportionally influencing the model. The models I
                will be comparing are:
                """)
    st.markdown("""- **Model A:** Baseline linear regression (raw
                data)\n - **Model B:** Pipeline with feature scaling
                """)
    st.subheader("Model Performance Comparison")

    baseline_r2 = 0.83
    baseline_rmse = 4.48

    pipeline_r2 = 0.83
    pipeline_rmse = 4.48

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Baseline R²", baseline_r2)
        st.metric("Baseline RMSE", baseline_rmse)

    with col2:
        st.metric("Pipeline R²", pipeline_r2)
        st.metric("Pipeline RMSE", pipeline_rmse)

    st.markdown("### Interpretation")
                
    st.markdown("""Both the baseline model and the fully processed pipeline
                achieved **identical performance** (**R² = 0.83**, **RMSE =
                4.48**). This result is expected for an **Ordinary Least
                Squares (OLS) linear regression model**. OLS is
                **scale-invariant**, meaning that applying feature
                scaling does not change the model's predictions or its
                accuracy metrics. The model simply adjusts its coefficients
                to compensate for any scaling applied to the input features.
                """)

    st.markdown("### Conclusion")

    st.error("""Preprocessing did **not** improve performance because the
               dataset was already clean, fully numerical, and appropriately
               scaled for OLS regression. Therefore, the baseline and
               pipeline models perform equivalently, and **Hypothesis 4 is
               not supported**.
               """)

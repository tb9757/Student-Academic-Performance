# Student Academic Performance

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Dataset Content

-   This is a synthetic dataset containing student academic metrics for 2000 individual pupils. The dataset includes attendance, internal exam scores, assignment performance, daily study habits, and final exam marks.

## Business Requirements

-   The school needs to understand whether final exam performance can be predicted using available student data, including metrics such as attendance, assignment performance, study habits, and internal test results.
    Purpose: To enable early identification of students at risk of underperforming so that interventions can be put in place.

-   The School would like to determine which factors have the biggest influence on high final exam marks.
    Purpose: To provide focus for school-wide strategy and resource allocation — for example, whether to prioritise improving attendance, strengthening homework routines, or focusing on internal assessment preparation.

## Hypothesis and how to validate?

**Hypothesis 1:** Average internal test score is more strongly correlated with final exam mark than attendance.

This hypothesis addresses the importance of being consistently in school versus performing well in internal assessments. It is comparing engagement and consistency with academic ability and prior knowledge.
I will validate this by comparing correlation coefficients for:

-   Attendance and final test scores.
-   Average internal test scores and final test scores.

**Hypothesis 2:** Average internal test scores (prior academic performance) explain more variance in final exam marks than engagement based behaviours, such as attendance, assignment score, and daily study hours.

-   This hypothesis can be tested by fitting a linear regression model using all available data.
-   The model's coefficient will be examined to see which variables contribute most to predicting final exam marks.
-   The size of the coefficients will be compared for the engagement related metrics and the prior attainment metrics.

**Hypothesis 3:** Students studying for more than 3 hours per day have significantly higher final exam marks than those who study 3 hours or fewer.

-   The dataset will be split into two groups based on daily study time.
-   The distributions of final exam marks will be be compared for these two groups to determine if there is a statistically significiant difference.
-   Both groups data will be checked for normality. If they are normally distributed then a t-test will be used, if not then a Mann-Whitney U test is applicable.

**Hypothesis 4:** A regression model that includes preprocessing steps (such as scaling) will perform better than a model trained on the raw data.

-   A basic linear regression model will be trained on the raw dataset with no preprocessing.

-   A second model will be trained using a full regression pipeline that includes scaling.

-   The performance of both models will be compared using standard regression metrics such as R2, Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).

-   Lower error values will indicate better performance

## Project Plan

-   My plan is to clean the data and then understand it with some simple visualisations, with a focus on distributions so that I can understand what statistical tests to perform
-   I want to know what effect studying has on their results so I intend to split pupils into a high study group and a low study group
-   I will then use linear regression as a predictive model.
-   Regression will also give me an idea of which factors have the biggest effect on final exam marks.
-   I also would like to practice building an ML pipeline, so my plan is to build a pipeline version and compare it to a non-pipeline to see which perfoms better.
-   I also want to gain skills in building a streamlit app so I will be doing this to build the dashboard.

## The rationale to map the business requirements to the Data Visualisations

To ensure that each business requirement could be answered clearly and supported by evidence, appropriate data visualisations were selected based on the type of insight required.

Business Requirement 1

The school needs to understand whether final exam performance can be predicted using available student data.

This requirement focuses on predictability and overall model performance. It was addressed using:

-   Scatter plots with trendlines, to visually assess linear relationships between final exam marks and key predictors such as attendance, study hours, and internal test scores.

-   Correlation heatmaps, to summarise the strength and direction of relationships across all numerical variables and identify which features are most strongly associated with final exam performance.

-   Regression model performance metrics (R² and RMSE), displayed visually, to quantify how well final exam marks can be predicted using the available data.

Together, these visualisations allow stakeholders to understand both whether prediction is feasible and how accurate those predictions are, supporting early identification of students at risk of underperforming.

Business Requirement 2

The school would like to determine which factors have the biggest influence on high final exam marks.

This requirement focuses on explanation and prioritisation rather than prediction alone. It was addressed using:

-   Regression coefficient visualisations, to show the relative contribution of each predictor variable to final exam marks in an interpretable way.

-   Comparative plots and grouped distributions, to visually compare outcomes across different engagement and study behaviour levels.

-   Model comparison metrics, to demonstrate how including academically relevant features (such as internal test scores) improves explanatory power compared to engagement-only models.

These visualisations support evidence-based decision-making by highlighting which factors contribute most strongly to high performance, helping inform school-wide strategies and resource allocation.

## Analysis techniques used

This project involves a range of different analysis techniques:

-   Data cleaning, checking for null values and duplicate rows
-   Feature engineering, average test scores column and categorisation of pupils into high and low study groups
-   Assessing data distribution with histograms
-   Using scatter charts to assess correlaion between features
-   Assessing correlation using both Pearson and Spearman techniques and visualising these in correlation heatmaps
-   Using the Mann-Whiteney U statistical test to assess the difference between two groups
-   Performing linear regression and increasing the complexity of the model by building a pipeline

A limiting factor of the dataset is its size. A larger dataset could have given more interesting and robust insights.

I also felt limited by the synthetic nature of the dataset. The dataset has been designed to be a teaching tool to help understand and practice linear regression. Any conclusions made are valid but maybe not as interesting as if the dataset was actual pupil data. This would have created more complex privacy issues and it is perfectly understandable that this kind of data is not made available to the public.

The techniques in this project could be used on real data by a school or an organisation and the results would provide meaningful and useful information with regards to the business requirements I have outlined.

Use generative AI tools:
I have found chat GPT to be useful throughout this project. Particularly in hypothesis generation and conclusion writing. For both of these I first came up with ideas and then asked chat GPT for help and refinement. This was very useful in making hypotheses because I wanted them to be meaningful and measurable in a useful way that also allowed me to practice techniques (like pipeline generation) without just doing ML for the sake of it. With conclusion I would type my interpretation of the results and ask GPT to evaluate my response. It was useful to bring to my attention any slight misunderstandings I had with the output values of linear regression or the statistical tests.

I also prompted chat GPT not to show me any code, but to act as a tutor/mentor and ask questions and give hints. I found this really helpful because I didn't want to fall into the trap of just copying code from AI and not understanding what the code does.

visualisation types
stats / hypothesis testing
machine learning linear regression

## Ethical considerations

-   This dataset was synthetic, so none of the data were related to any real pupils.
-   Despite this I removed the student ID tag as this would be good practice with a real dataset in order to annonomyse the data.

## Dashboard Design

-   List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
-   Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
-   How were data insights communicated to technical and non-technical audiences?
-   Explain how the dashboard was designed to communicate complex data insights to different audiences.

## Unfixed Bugs

-   Please mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
-   Did you recognise gaps in your knowledge, and how did you address them?
    Swapping linear regression for lasso - didn't fully understand why, have added a description from gpt
-   If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

## Development Roadmap

-   What challenges did you face, and what strategies were used to overcome these challenges?

initially thought the distributions were normal because of small skew values. when checked for normality later they were found not to be normal so had to switch from pearson to spearman, and had to do a new correlation heatmap (left the old one in)

feature selection dropping all of the features, so swiitching to lasso

-   What new skills or tools do you plan to learn next based on your project experience?

I would like to continue my ML journey with the following

-   a classification project
-   an unsupervised project
-   some sort of cross validation
-   !!!!!!!!!!!!!!!!! whats the one where you get the machine to pick the correct algo

## Deployment

### Heroku

-   The App live link is: https://YOUR_APP_NAME.herokuapp.com/
-   Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
-   The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. From the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis Libraries

-   **Pandas:** used throughout this project, in essential data analysis tasks such as: reading data into dataframes, adding new features as columns, dropping columns, changing datatypes, checking for null values and duplicates.
-   **Matplotlib:** foundation for most visualisations, useful for seetting chart titles and displaying the charts.
-   **Seaborn:** to make visually appealing charts to assess: distributions of results, the correlation between different variables in a correlation heatmap, and a pairplot to get a feel for all of the data.
-   **Numpy:** foundation for all data manipulation but specifically used to take the square root of the mean squared error for the regression model.
-   **Plotly:** to make interactive scatterplots to demonstrate the relationship between two parameters for hypothesis 1.
-   **Scikit learn:** for the machine learning section. Used for the linear regression tasks and was essential in addressing hypothesis 2 and 4.

## Conclusions

## Credits

A huge source of help for this project was the code institute LMS. It was particularly helpful to follow through the the machine learning section. I gathered information on how to construct a pipeline and the steps to take to evaluate its results.

There are some sections of my code which I copied directly from the LMS, and I have referenced this in comments where I have done this. I will also list them here:

-   Removing the duplicate side from a correlation heatmap whilst testing hypothesis 1
-   The code to display the histogram and boxplot whilst investigating hypotheses 3. This is lifted straight from the LMS, it provides a dotted red line to show the mean value for each group - easier to directly compare whilst plotting a box plot on the side.

Useful websites:

-   Documentation page for scikit learn when trying to understand the difference between Lasso linear regression and ordinary least squares regression.
-   Documentation page for seaborn when picking a colour for the correlation heatmap that would help pick out the differences between high and low correlation.
-   Streamlit website for how to do metrics https://docs.streamlit.io/develop/api-reference/data/st.metric

Chat GPT has been helpful along the way in many ways, but I will list the main ways I have been using it below:

Note: I told it not to show me code, just to ask me questions and give me hints, because I wanted to learn how everything works, not just copy generated code. I found this to be successful as it felt like a course mentor.

-   Hypothesis refinement and ideation
-   General debugging of code
-   Sense checking thoughts on where to head next with analysis
-   Understanding the meaning of the ML output

### Content

-   The text for the Home page was taken from Wikipedia Article A
-   Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
-   The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

-   The photos used on the home and sign-up page are from This Open-Source site
-   The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)

-   Thanks to Emma, my coursemates and the instructors.

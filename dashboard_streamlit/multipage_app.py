import streamlit as st
from app_pages.multi_page import MultiPage

# load pages scripts
from app_pages.page1 import page1_body
from app_pages.page2 import page2_body

app = MultiPage(app_name= "Student Academic Performance")  # Create an instance

# Add your app pages here using .add_page()
app.add_page("Data Overview", page1_body)
app.add_page("Hypothesis 1", page2_body)

app.run() # Run the  app
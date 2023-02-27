
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data.csv")

# Set page title
st.set_page_config(page_title="My App")

# Add a title
st.title("My Streamlit App")

# Add a slider to select a value
x = st.slider("Select a value", 0, 10)

# Create a plot using Plotly Express
fig = px.line(df, x="x", y="y", range_x=[0, 10], range_y=[0, 10])

# Update plot based on slider value
fig.update_traces(x=[x, x])

# Show plot
st.plotly_chart(fig)


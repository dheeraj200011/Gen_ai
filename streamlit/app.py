import streamlit as st
import pandas as pd
import numpy as np

## tiltle of the app
st.title("Hello Dheeraj 👋")

## create plain text
st.write("Streamlit successfully working!")

# Display a dataframe

st.write("here is the dataframe")

## create a dataframe

data = {
    "Name": ["Dheeraj", "Rahul", "Amit"],
    "Age": [25, 28, 30],
    "City": ["Kanpur", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)

st.write(df)

## create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=["a","b","c"]
)

st.line_chart(chart_data)
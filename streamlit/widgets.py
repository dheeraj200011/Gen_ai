import streamlit as st
import pandas as pd 

st.title("Streamlit text input")

name = st.text_input("Enter name")

age = st.slider("select your age:", 0, 100, 31)

selectbox = st.selectbox("Select a name", ["Dheeraj", "Priya", "Suresh"])

st.write(f"your name is {selectbox}")

if name:
    st.write(name)
else:
    st.write("")
    
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    # remove unwanted unnamed columns
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    st.dataframe(df)
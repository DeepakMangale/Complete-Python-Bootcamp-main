import streamlit as st
import pandas as pd 

st.title("Streamlit Text input")
name = st.text_input("Enter your name")

age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is {age}")

option = ["Option 1", "Option 2", "Option 3"]
choice = st.selectbox("Choose an option", option)
st.write(f"You selected: {choice}")

if name:
    st.write (f"hello {name}!")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)

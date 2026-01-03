import streamlit as st
import pandas as pd
import numpy as np  

## title of the application 
st.title("Simple Data Analysis App")

## display a simple text
st.write("This is a simple text ")

## create a dataframe
df = pd.DataFrame ({
    '1 column': [1, 2, 3, 4],
    '2 column': [10, 20, 30, 40]
})

## display the dataframe
st.write("Here is a simple dataframe:")
st.write(df)

## create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
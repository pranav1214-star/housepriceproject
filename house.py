import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('House Price ANALYSIS')
st.subheader('{House Price Predicition}')

try:
    df = pd.read_csv('data.csv')
except FileNotFoundError:
    st.error('File not found. Please check the file path.')
    st.stop()
except pd.errors.EmptyDataError:
    st.error('File is empty. please make sure it is proper.')
    st.stop()
except Exception as e:
    st.error(f'An unexpected error occurred: {e}')
    st.stop()
# 
df = pd.read_csv('data.csv')
st.header("House Price Predicition Data File")
if st.button('Open File'):
    st.write(df)
st.write('Click button to use shape function')
if st.button("Click here"):
    st.markdown(df.shape)
#
try:
    st.header('Dataset:')
    dataset = pd.read_csv('data.csv')
    st.subheader(f'[Total records before cleaning:-  {len(dataset)}]')
    dataset = dataset.drop_duplicates()
    st.subheader(f'[Total records after removing duplicates:-  {len(dataset)}]')
    st.write('')
    st.subheader('Head Function Implementation')
    st.write('')
    if st.button('Click to implement head() function'):
        st.write(dataset.head(10))
    st.write('')    
    st.subheader('Tail Function Implementation')
    st.write('')
    if st.button('Click to implement tail() function'):
        st.write(dataset.tail())
    st.write('')    
    st.subheader('Describe Function Implementation')
    st.write('')
    if st.button('Click here to implement describe function'):
        st.write(dataset.describe())
    st.write('')    
        
except Exception as e:
    st.error(f'An error occurred while cleaning the dataset: {e}')
    st.stop()




st.subheader('Bar Chart Example')
column = st.sidebar.selectbox('Select Column', df.columns,index=2)

if column == 0:
    st.error('Please select different columns for X and Y axis.')
else:

    st.subheader('Bar Chart')
    st.bar_chart(df[column].head(10))

    st.subheader('Line Chart Example')
    st.subheader('Line Chart')
    st.line_chart(df[column].head(10))
    
    st.subheader('Scatter Plot Example')
    st.subheader('Scatter Plot')
    st.scatter_chart(df[column].head(10))

    st.subheader("Pie chart using matplotlib")
    plt.pie(df['bedrooms '].value_counts().values,autopct='%1.1f%%',labels=df['bedrooms '].value_counts().index)
    st.pyplot(plt)
    

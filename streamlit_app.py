import streamlit as st
import pandas as pd
st.title('Machine Learning App')
st.info("This is app build models")
with st.expander('Data'):
  st.write('**Raw Data**')
  columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
  df = pd.read_csv("bezdekIris.data", header=None, names=columns)
  st.write(df)  # Display the data

# Display the features (X)
st.write('**X (Features)**')
x = df.drop("species",axis=1)
x
st.write('**Y (Features)**')
y = df['species']

with st.expander('Data Visualization'):
  st.scatter_chart(data = df, x="sepal_width",y="species",color = "species")

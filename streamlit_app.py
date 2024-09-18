import streamlit as st
import pandas as pd
st.title('Machine Learning App')
st.info("This is app build models")
with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv("bezdekIris.data")
  df
st.write('**X**")
x = df[:-1]


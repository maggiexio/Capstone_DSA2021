import streamlit as st
import pandas as pd
import plotly.express as px

#define functions
@st.cache
def raw_data (input_file):
  df=pd.read.csv(input_file)
  return df

#title
st.title("Data Excursion for DSA Capstone Project:)
st.markdown("This Dashboard is designed for the capstone project of DSA 2021-2022")
st.markdown ("By: Maggie Xiong") 
st.latex(r'''R_{\mu\nu} - \frac{1}{2}Rg_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}''')
         
         
# read in data
df_ori=raw_data("data_capstone_dsa2021_2022.csv")
         
with st.expander("Display the data"): 
         st.dataframe(df_ori)
         
#sidebar
st.sidebar.markdown("## Filter the data")
score_1, score_2 = st.sidebar.slider("please select age range", 10, 20, (10,20))    
df_1=df_ori.querry("age>=score_1 and age<=@score_2")
         
st.markdown('##Data Visualizaion')
fig_hist=px.hostogram(df_1, x='sum_score', color='gender', facet_row='home_computer')
st.plotly_chart(fig_hist, height=1000)
         
#Ballon
a1, a2, a3=st.columns(3)
clicks=a2.button('click to celebrate')
if clicks:
         st.ballons()

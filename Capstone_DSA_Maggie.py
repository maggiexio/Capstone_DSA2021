import streamlit as st
import pandas as pd
import plotly.express as px

#define functions
@st.cache
def raw_data (input_file):
  df=pd.read_csv(input_file)
  return df

#title
st.title("Data Excursion")
st.header("DSA Capstone Project")
st.markdown("This Dashboard is designed for the capstone project of DSA 2021-2022")
st.markdown ("By: Maggie Xiong") 
#st.latex(r'''R_{\mu\nu} - \frac{1}{2}Rg_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}''')
         
         
# read in data
df_ori=raw_data("data_capstone_dsa2021_2022.csv")
         
with st.expander("Display the data"): 
         st.dataframe(df_ori)
         
#sidebar
df_1=df_ori
st.sidebar.markdown("## Define **filters:**")
score_1, score_2 = st.sidebar.slider("Total score: ", min(df_ori.sum_score), max(df_ori.sum_score), (min(df_ori.sum_score), max(df_ori.sum_score)))
df_1=df_1.query("sum_score>=@score_1 and sum_score<=@score_2")
time_1, time_2 = st.sidebar.slider("Total response time",  min(df_ori.rt_total), max(df_ori.rt_total), (min(df_ori.rt_total), max(df_ori.rt_total)))    
df_1=df_1.query("rt_total>=@time_1 and rt_total<=@time_2")
age_1, age_2 = st.sidebar.slider("Age range",  min(df_ori.age), max(df_ori.age), (min(df_ori.age), max(df_ori.age)))    
df_1=df_1.query("age>=@age_1 and age<=@age_2")
         
title_ch1='##Data Visualizaion'
st.markdown(f'<h1 style="text-aligh: center;color: red;">{title_ch1}</h1>',unsafe_allow_html=True')
fig_hist=px.histogram(df_1, x='sum_score', color='gender', facet_row='home_computer')
st.plotly_chart(fig_hist, height=1000)
         
#Ballon
a1, a2, a3=st.columns(3)
clicks=a2.button('click to celebrate')
if clicks:
         st.ballons()

import streamlit as st
import pandas as pd
import plotly.express as px

#define functions
def Turn_DICT_Uppercase(dic):
  return {k.upper():v.upper() for k,v in dic.items()}

def Find_State_Country(state_name):
  us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
   }
  country_abbrev={
    "Canada": "CA",
    "United State of America": "USA",
  }
  us_state_to_abbrev=Turn_DICT_Uppercase(us_state_to_abbrev)
  country_abbrev=Turn_DICT_Uppercase(country_abbrev)

  name=name.replace(',',' ',)
  state=''
  country=''
  for t in set(name.split()):
      if t.upper() in us_state_to_abbrev.keys():
          state=us_state_to_abbrev[t.upper()]
      if  t.upper() in us_state_to_abbrev.values():
          state=t.upper()
      if t.upper() in country_abbrev.keys():
          country=country_abbrev[t.upper()]
      if  t.upper() in country_abbrev.values():
          country=t.upper()  
  return state, country
    
   

@st.cache
def raw_data(input_file):
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
for state_ori in df_ori.state:
  df_ori.state_abbr, df_ori.country_abbr = Find_State_Country(state_ori)
         
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
         
title_ch1='Data Visualizaion'
st.markdown(f'<h2 style="text-aligh: center;color: red;">{title_ch1}</h2>',unsafe_allow_html=True)
fig_hist1=px.histogram(df_1, x='sum_score', color='gender', facet_col='home_computer')
st.plotly_chart(fig_hist1, height=600)
fig_hist2=px.histogram(df_1, x='sum_score', animation_frame='state_abbr')
st.plotly_chart(fig_hist2, height=600)
         
#Ballon
a1, a2, a3=st.columns(3)
clicks=a2.button('click to celebrate')
if clicks:
         st.ballons()

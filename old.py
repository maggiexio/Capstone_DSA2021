import streamlit as st
import pandas as pd
import plotly
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
    "United States of America": "USA",
  }
  us_state_to_abbrev=Turn_DICT_Uppercase(us_state_to_abbrev)
  country_abbrev=Turn_DICT_Uppercase(country_abbrev)

  state_name=state_name.replace(',',' ',)
  state=''
  country='USA'
  for t in set(state_name.split()):
      if t.upper() in us_state_to_abbrev.keys():
          state=us_state_to_abbrev[t.upper()]
      if  t.upper() in us_state_to_abbrev.values():
          state=t.upper()
      if t.upper() in country_abbrev.keys():
          country=country_abbrev[t.upper()]
      if  t.upper() in country_abbrev.values():
          country=t.upper()  
  return state, country
    
   

#@st.cache
def raw_data(input_file):
  df=pd.read_csv(input_file)
  return df

#######################text part
#st.title("Data Excursion")
title_1="Data Excursion"
st.markdown(f'<h1 style="text-aligh: center;color: green;">{title_1}</h1>',unsafe_allow_html=True)
#st.header("DSA Capstone Project")
subj_1="          -- DSA Capstone Project"
st.markdown(f'<h2 style="text-aligh: center;color: green;">{subj_1}</h2>',unsafe_allow_html=True)
st.markdown("This Dashboard is designed for the capstone project of DSA 2021-2022")
st.markdown ("By: Maggie Xiong") 
#st.latex(r'''R_{\mu\nu} - \frac{1}{2}Rg_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}''')
         
         
# read in data
df_ori=raw_data("data_capstone_dsa2021_2022.csv")
df_ori['rt_gs_1']=""
df_ori['state_abbr']=""
df_ori['country_abbr']=""
for i, state_ori in enumerate(df_ori.state):
  df_ori['state_abbr'][i], df_ori['country_abbr'][i] = Find_State_Country(state_ori)

df_ori_1=df_ori.iloc[:,[45,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,46,47,44]]  
with st.expander("Data view"): 
         st.dataframe(df_ori_1)
         
# Filters
df_1=df_ori
st.sidebar.markdown("## Define **filters:**")
score_1, score_2 = st.sidebar.slider("Total score: ", min(df_ori.sum_score), max(df_ori.sum_score), (min(df_ori.sum_score), max(df_ori.sum_score)))
df_1=df_1.query("sum_score>=@score_1 and sum_score<=@score_2")
time_1, time_2 = st.sidebar.slider("Total response time (note: response time for the first item is missing hence excluded",  min(df_ori.rt_total), max(df_ori.rt_total), (min(df_ori.rt_total), max(df_ori.rt_total)))    
df_1=df_1.query("rt_total>=@time_1 and rt_total<=@time_2")
age_1, age_2 = st.sidebar.slider("Age range",  min(df_ori.age), max(df_ori.age), (min(df_ori.age), max(df_ori.age)))    
df_1=df_1.query("age>=@age_1 and age<=@age_2")
#sex=df_1['gender'].drop_duplicates()
#mode=df_1['home_computer'].drop_duplicates()
sex_choice = st.sidebar.selectbox('Select gender:', ['All', 'Male', 'Female'])
if sex_choice != "All":
  df_1=df_1.query("gender==@sex_choice")
mode_choice = st.sidebar.radio('Whether take the test at home:', ['All', 'Yes', 'No'])
if mode_choice != "All":
  df_1=df_1.query("home_computer==@mode_choice")
#radio1=st.radio('Navigation', ['All', 'Yes', 'No'], index=1)
#if mode_choice != "All":
#  df_1=df_1.query("home_computer==@radio1")



title_ch1='Data Visualizaion'
st.markdown(f'<h3 style="text-aligh: center;color: green;">{title_ch1}</h3>',unsafe_allow_html=True)
title_ch2='****2D interactive plots********'
st.markdown(f'<h4 style="text-aligh: center;color: green;">{title_ch2}</h4>',unsafe_allow_html=True)
fig_hist1=px.histogram(df_1, x='sum_score', color='gender', facet_col='home_computer')
st.plotly_chart(fig_hist1, height=600)
fig_hist2=px.histogram(df_1, x='sum_score', animation_frame='state_abbr')
st.plotly_chart(fig_hist2, height=600)
fig_3=px.sunburst(df_1, color='sum_score',  path=['country_abbr','state_abbr'])
st.plotly_chart(fig_3, height=600)
fig_4=px.choropleth(df_1, color='sum_score',  locations='country_abbr')
st.plotly_chart(fig_4, height=600)
title_ch3='****3D interactive plots********'
st.markdown(f'<h4 style="text-aligh: center;color: green;">{title_ch3}</h4>',unsafe_allow_html=True)
fig_scatter1=px.scatter_3d(df_1, y='sum_score', x='age', z='home_computer', color='gender', size='rt_total')
st.plotly_chart(fig_scatter1, height=1500)

        
#Ballon
a1, a2, a3=st.columns(3)
clicks=a2.button('Export the figure')
if clicks:
  fig_scatter1.write_html('scatterplot.html')
#         st.ballons()

import streamlit as st
import pandas as pd
import numpy as np
from functions import *

dic = {'Sunrisers Hyderabad': 'SRH', 'Kolkata Knight Riders': 'KKR',
       'Royal Challengers Bangalore': 'RCB', 'Kings XI Punjab': 'KXIP',
       'Mumbai Indians': 'MI', 'Chennai Super Kings': 'CSK',
       'Rajasthan Royals': 'RR', 'Delhi Capitals': 'DC'
       }

st.title("IPL Dashboard")

st.write("Winning percentage for each team")
st.plotly_chart(winningPercentage())

st.write("Team in most seasons")
st.plotly_chart(team_in_most_season())

st.write("Most player of the matches")
st.plotly_chart(player_match_season())

st.write("key player for each team")

option = st.selectbox("Enter team name", ("Sunrisers Hyderabad",
                                "Kolkata Knight Riders",
                                "Royal Challengers Bangalore",
                                "Kings XI Punjab",
                                "Mumbai Indians", 
                                "Chennai Super Kings",
                                "Rajasthan Royals",
                                "Delhi Capitals"))

st.plotly_chart(key_player_team(dic[option]))

st.write("Winning percentage by toss decision")
st.plotly_chart(win_visu_by_toss(dic[option]))

import streamlit as st
from functions import Cleaner, winningPercentage, team_in_most_season, player_match_season, win_visu_by_toss

# Basic Initialization
cleaner_obj = Cleaner()
cleaner_obj.clean_inconsistent_teams()
cleaner_obj.replace_team_shortforms()


dic = {'Sunrisers Hyderabad': 'SRH', 'Kolkata Knight Riders': 'KKR',
       'Royal Challengers Bangalore': 'RCB', 'Kings XI Punjab': 'KXIP',
       'Mumbai Indians': 'MI', 'Chennai Super Kings': 'CSK',
       'Rajasthan Royals': 'RR', 'Delhi Capitals': 'DC'
       }

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>IPL Dashboard</h1>",
            unsafe_allow_html=True)

st.text("")
st.text("")

# Sidebar
st.sidebar.markdown("### Parameters")
season_labels = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

team1 = st.sidebar.selectbox("Team-1", dic.keys())
team2 = st.sidebar.selectbox("Team-2", dic.keys(), index=1)
season = st.sidebar.multiselect("Seasons", season_labels, season_labels)

container1 = st.container()
col1, col2 = st.columns(2)

with container1:
       with col1:
              # ---------------
              # Pie Plot
              st.markdown("<p style='text-align: center;'>Winning percentage between both teams</p>",
                     unsafe_allow_html=True)
              st.plotly_chart(winningPercentage(dic[team1], dic[team2], cleaner_obj, season), use_container_width=True)
              st.text("")
              st.text("")
       
       with col2:
              # -----------------
              # histogram plot
              st.markdown("<p style='text-align: center;'>Match Count in each Season</p>",
                     unsafe_allow_html=True)
              st.plotly_chart(team_in_most_season(dic[team1], dic[team2], cleaner_obj, season), use_container_width=True)
              st.text("")
              st.text("")

# ------------------
# histogram
st.markdown("<p style='text-align: center;'>Most player of the matches</p>",
            unsafe_allow_html=True)
st.plotly_chart(player_match_season(dic[team1], dic[team2], cleaner_obj, season), use_container_width=True)
st.text("")
st.text("")

# ---------------------
# pie
st.markdown("<p style='text-align: center;'>Winning percentage by toss decision</p>", unsafe_allow_html=True)
container2 = st.container()
col3, col4 = st.columns(2)

with container2:
       with col3:
              st.plotly_chart(win_visu_by_toss(dic[team1], cleaner_obj, season), use_container_width=True)
       with col4:
              st.plotly_chart(win_visu_by_toss(dic[team2], cleaner_obj, season), use_container_width=True)

st.text("")
st.text("")

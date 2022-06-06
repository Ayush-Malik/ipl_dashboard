import streamlit as st
import streamlit.components.v1 as components
from functions import Cleaner, Cards, winningPercentage, team_in_most_season, player_match_season, win_visu_by_toss

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

st.markdown("<marquee ><h1 style='text-align: center; font-size : 70px; text-decoration: underline;'>IPL Dashboard</h1> </marquee>",
            unsafe_allow_html=True)

st.text("")
st.text("")

# Sidebar
st.sidebar.markdown("### Parameters")
season_labels = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

team1 = st.sidebar.selectbox("Team-1", dic.keys())
team2 = st.sidebar.selectbox("Team-2", dic.keys(), index=1)
season = st.sidebar.multiselect("Seasons", season_labels, season_labels)

card_obj = Cards(cleaner_obj, season)
total_matches_one = card_obj.total_matches(dic[team1])
total_matches_win_one = card_obj.total_matches_win(dic[team1])
best_season_one = card_obj.best_season(dic[team1])

# for second team
total_matches_second = card_obj.total_matches(dic[team2])
total_matches_win_second = card_obj.total_matches_win(dic[team2])
best_season_second = card_obj.best_season(dic[team2])

# bootstrap 4 cards to be shown on top of ipl dashboard
components.html(
       """
       <head>
              <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
              <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
              <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
       </head>
       
       <body style="background-color: #0e1118;">
              <div class="row mt-2 pt-2 mb-2 pt-2">
                     <div class="col-sm-4 col-4" >
                            <div class="card text-white bg-dark border-secondary" style="width: 20rem; left:2.5rem;">
                                   <div class="card-body">
                                          <marquee direction='up' behavior='alternate'> <h5 class="card-title" style="text-align: center;">Total Matches</h5> </marquee>
                                          <p class="card-text" style="font-size:3rem; text-align: center;"><span style="color: #1aa3ff;">""" 
                                          + str(total_matches_one) + "</span>" + " | " + "<span style='color: #ff471a;'>" + str(total_matches_second) + "</span>" + """</p>
                                   </div>
                            </div>
                     </div>
                     <div class="col-sm-4 col-4">
                            <div class="card text-white bg-dark border-secondary" style="max-width: 20rem; left:2.5rem;">
                                   <div class="card-body">
                                          <marquee direction='up' behavior='alternate'><h5 class="card-title" style="text-align: center;">Total Matches Wins</h5></marquee>
                                          <p class="card-text" style="font-size:3rem; text-align: center;"><span style="color: #1aa3ff;">""" + str(total_matches_win_one) + "</span>" + " | " + "<span style='color: #ff471a;'>" + str(total_matches_win_second) + "</span>" +"""</p>
                                   </div>
                            </div>
                     </div>
                     <div class="col-sm-4 col-4">
                            <div class="card text-white bg-dark border-secondary" style="max-width: 20rem; left:2.5rem;">
                                   <div class="card-body">
                                          <marquee direction='up' behavior='alternate'><h5 class="card-title" style="text-align: center;">Best Season</h5> </marquee>
                                          <p class="card-text" style="font-size:3rem; text-align: center;"><span style="color: #1aa3ff;">"""+ str(best_season_one) + "</span>" + " | " + "<span style='color: #ff471a;'>" + str(best_season_second) + "</span>" +"""</p>
                                   </div>
                            </div>
                     </div>
              </div>
       </body>

       """,
       height=300,
)


# ------------------
# histogram
st.markdown("<p style='text-align: center; font-size:60px; text-decoration: underline;'>Most  player  of  the  matches</p>",
            unsafe_allow_html=True)
st.plotly_chart(player_match_season(dic[team1], dic[team2], cleaner_obj, season), use_container_width=True)
for i in range(12):
       st.text("")


# ---------------------
# pie
st.markdown("<p style='text-align: center; font-size:60px; text-decoration: underline;'>Winning  percentage  by  toss  decision</p>", unsafe_allow_html=True)
container2 = st.container()
col3, col4 = st.columns(2)

with container2:
       with col3:
              st.plotly_chart(win_visu_by_toss(dic[team1], cleaner_obj, season), use_container_width=True)
       with col4:
              st.plotly_chart(win_visu_by_toss(dic[team2], cleaner_obj, season), use_container_width=True)

for i in range(12):
       st.text("")


# -----------------
# histogram plot
st.markdown("<p style='text-align: center; font-size:60px; text-decoration: underline;'>Match  Count  in  each  Season</p>",
       unsafe_allow_html=True)
st.plotly_chart(team_in_most_season(dic[team1], dic[team2], cleaner_obj, season), use_container_width=True)

for i in range(12):
       st.text("")

# ---------------
# Pie Plot
st.markdown("<p style='text-align: center; font-size:60px; text-decoration: underline;'>Winning  percentage  between  both  teams</p>",
       unsafe_allow_html=True)
st.plotly_chart(winningPercentage(dic[team1], dic[team2], cleaner_obj, season), use_container_width=True)
st.text("")
st.text("")
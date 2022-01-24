import pandas as pd
import plotly.express as px
import pandas as pd
import numpy as np

color_ls = ["#e056fd", "#434343", "#e84393", "#5e5368"]

matches = pd.read_csv(r'E:\5th_sem_proj\ipl_dashboard\matches.csv')

matches.replace(to_replace=['Delhi Daredevils'], value=['Delhi Capitals'], inplace=True)

consistent_teams = ['Sunrisers Hyderabad', 'Mumbai Indians',
                    'Kolkata Knight Riders', 'Royal Challengers Bangalore',
                    'Delhi Capitals', 'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals']


# Taking data of only consistent teams
matches_2 = matches[(matches.team1.isin(consistent_teams))
                    & (matches.team2.isin(consistent_teams))]

dic = {'Sunrisers Hyderabad': 'SRH', 'Kolkata Knight Riders': 'KKR',
       'Royal Challengers Bangalore': 'RCB', 'Kings XI Punjab': 'KXIP',
       'Mumbai Indians': 'MI', 'Chennai Super Kings': 'CSK',
       'Rajasthan Royals': 'RR', 'Delhi Capitals': 'DC'
       }

# Replacing names of teams to their short names
matches_2.replace(dic, inplace=True)

def winningPercentage(team_1, team_2):
    win_prcntage = (matches_2.winner.value_counts() / (matches_2.team1.value_counts() + matches_2.team2.value_counts())) * 100
    
    win_prcntage = pd.DataFrame({
        'Team_Name': [team_1, team_2],
        'Win %age': [win_prcntage[team_1], win_prcntage[team_2]]
    })
    
    fig = px.pie(win_prcntage, names='Team_Name', values='Win %age', hole=0.3,
                 color="Team_Name", color_discrete_map={team_1: "#e84393", team_2: "#434343"})
    return fig


def team_in_most_season(team_1, team_2):
    series_1 = matches_2.loc[matches_2["team1"] == team_1].season.value_counts()
    series_2 = matches_2.loc[matches_2["team1"] == team_2].season.value_counts()
    
    df1 = pd.DataFrame({
        "Team_name": [team_1 for i in range(len(list(series_1.keys())))],
        "Season": list(series_1.keys()),
        "Match Count": list(dict(series_1).values()),
    })
    
    df2 = pd.DataFrame({
        "Team_name": [team_2 for i in range(len(list(series_2.keys())))],
        "Season": list(series_2.keys()),
        "Match Count": list(dict(series_2).values()),
    })
    
    df = pd.concat([df1, df2], ignore_index=True)
    
    fig = px.histogram(df, x='Season', y='Match Count', color="Team_name",
                       barmode="group", color_discrete_map={team_1: "#55efc4", team_2: "#e84393"})
    
    return fig

def player_match_season(team_1, team_2):
    series_1 = matches_2.loc[matches_2["team1"] == team_1].player_of_match.value_counts()[:5]
    series_2 = matches_2.loc[matches_2["team1"] == team_2].player_of_match.value_counts()[:5]
    
    df1 = pd.DataFrame({
        "Team_name": [team_1 for i in range(len(list(series_1.keys())))],
        "Player Name": list(series_1.keys()),
        "Match Count": list(dict(series_1).values()),
    })
    
    df2 = pd.DataFrame({
        "Team_name": [team_2 for i in range(len(list(series_2.keys())))],
        "Player Name": list(series_2.keys()),
        "Match Count": list(dict(series_2).values()),
    })
    
    df = pd.concat([df1, df2], ignore_index=True)
    
    fig = px.histogram(df, x='Player Name', y='Match Count', color="Team_name",
                       barmode="group", color_discrete_map={team_1: "#55efc4", team_2: "#e84393"})
    
    return fig


dic = {'Sunrisers Hyderabad': 'SRH', 'Kolkata Knight Riders': 'KKR',
        'Royal Challengers Bangalore': 'RCB', 'Kings XI Punjab': 'KXIP',
        'Mumbai Indians': 'MI', 'Chennai Super Kings': 'CSK',
        'Rajasthan Royals': 'RR', 'Delhi Capitals': 'DC'
        }
matches.replace(dic, inplace=True)

def win_visu_by_toss(team_name):
    datas = matches[(matches['toss_winner']==team_name) & (matches['winner']==team_name)]
    count = datas['toss_decision'].value_counts()
    win_bat = count['bat']/(count['field']+count['bat'])*100
    win_field = count['field']/(count['bat']+count['field'])*100
    data = [['Fielding', win_field], ['Batting', win_bat]]
    data = pd.DataFrame (data,columns=['Decision','Win_%age'])
    
    fig = px.pie(data, values='Win_%age', names='Decision', title=team_name, hole=0.3, color="Decision", color_discrete_map={"Batting": "#e84393", "Fielding": "#434343"})
    return fig

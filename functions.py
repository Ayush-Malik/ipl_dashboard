import pandas as pd
import plotly.express as px
import pandas as pd
import numpy as np

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

def winningPercentage():
    win_prcntage = (matches_2.winner.value_counts() / (matches_2.team1.value_counts() + matches_2.team2.value_counts())) * 100
    
    pd.DataFrame({
        'Team_Name': list(dict(win_prcntage).keys()),
        'Win %age': list(dict(win_prcntage).values())
    })
    
    win_prcntage = win_prcntage.to_frame().reset_index().rename(columns={'index': 'Team_Name', 0: 'Win %age'})
    win_prcntage.sort_values(by='Win %age', ascending=False, inplace=True)
    
    fig = px.bar(win_prcntage, x = 'Team_Name', y = 'Win %age')
    return fig


def team_in_most_season():
    lis = matches_2.team1.unique()
    dic = {}
    
    for values in lis:
        dic[values] = 0
    
    for season_no in matches_2.groupby('season'):
        for team in dic:
            if team in season_no[1].team1.unique():
                dic[team] += 1
    
    team_vs_seasons = pd.DataFrame(dic.items()).rename(columns={0: 'Team Name', 1: 'Season Count'})
    team_vs_seasons.sort_values(by='Season Count', ascending=False, inplace=True)
    
    fig = px.pie(team_vs_seasons, names='Team Name', values='Season Count')
    
    return fig

def player_match_season():
    m_of_m_count = matches['player_of_match'].value_counts().head(15).to_frame().reset_index().rename(columns={'index': 'player_name', 'player_of_match': 'count'})
    
    fig = px.bar(m_of_m_count, x = 'player_name', y = 'count')
    
    return fig


dic = {'Sunrisers Hyderabad': 'SRH', 'Kolkata Knight Riders': 'KKR',
        'Royal Challengers Bangalore': 'RCB', 'Kings XI Punjab': 'KXIP',
        'Mumbai Indians': 'MI', 'Chennai Super Kings': 'CSK',
        'Rajasthan Royals': 'RR', 'Delhi Capitals': 'DC'
        }
matches.replace(dic, inplace=True)

def key_players(team_name):
    for value in matches.groupby('winner'):
        if value[0] == team_name:
            return value[1]['player_of_match'].value_counts().head()

def key_player_team(team_name):
    df = key_players(team_name).to_frame().reset_index().rename(columns={'index': 'Player', 'player_of_match': 'Count'})
    
    fig = px.bar(df, x='Player', y='Count')
    
    return fig

def win_visu_by_toss(team_name):
    datas = matches[(matches['toss_winner']==team_name) & (matches['winner']==team_name)]
    count = datas['toss_decision'].value_counts()
    win_bat = count['bat']/(count['field']+count['bat'])*100
    win_field = count['field']/(count['bat']+count['field'])*100
    print("field_count = "+ str(count['field']))
    print("bat_count = " + str(count['bat']))
    print("Win %age if fielding is choosen = " + str(win_field))
    print("Win %age if batting is choosen = " + str(win_bat))
    print()
    print()
    data = [['Fielding', win_field], ['Batting', win_bat]]
    data = pd.DataFrame (data,columns=['Decision','Win_%age'])
    
    fig = px.pie( data , values= 'Win_%age' , names='Decision', title='Win %age For '+ team_name + ' for toss decision',color_discrete_sequence=px.colors.sequential.Rainbow)
    return fig

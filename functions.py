import pandas as pd
import plotly.express as px

color_ls = ["#e056fd", "#434343", "#e84393", "#5e5368"]
season_ls = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

# --------------------------
#       Section - 1
#  -------------------------
## Cleaning and manipulation of data 
class Cleaner:
    new_df = None
    old_df = None
    
    def __init__(self) -> None:
        matches = pd.read_csv(r'E:\5th_sem_proj\ipl_dashboard\matches.csv')
        matches.replace(to_replace=['Delhi Daredevils'], value=['Delhi Capitals'], inplace=True)
        
        self.old_df = matches
        self.new_df = matches

    def get_teams(self):
        consistent_teams = ['Sunrisers Hyderabad', 'Mumbai Indians',
                            'Kolkata Knight Riders', 'Royal Challengers Bangalore',
                            'Delhi Capitals', 'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals']
        return consistent_teams

    def get_short_team_name(self):
        names = {'Sunrisers Hyderabad': 'SRH', 'Kolkata Knight Riders': 'KKR',
        'Royal Challengers Bangalore': 'RCB', 'Kings XI Punjab': 'KXIP',
        'Mumbai Indians': 'MI', 'Chennai Super Kings': 'CSK',
        'Rajasthan Royals': 'RR', 'Delhi Capitals': 'DC'}
        return names

    def clean_inconsistent_teams(self):
        # Taking data of only consistent teams and storing it into new dataframe
        self.new_df = self.old_df[(self.old_df.team1.isin(self.get_teams())) & (self.old_df.team2.isin(self.get_teams()))]

    def replace_team_shortforms(self):
        # Replacing names of teams to their short names
        names = self.get_short_team_name()
        self.new_df.replace(names, inplace=True)
        self.old_df.replace(names, inplace=True)

# -------------------------------
#          Section - 2
# -------------------------------
## Different Stats and data manipulation for Plots
def winningPercentage(team_1, team_2, cleaner_obj, season_ls):
    df = cleaner_obj.new_df
    df = df.loc[df["season"].isin(season_ls)]

    win_prcntage = (df.winner.value_counts() / (df.team1.value_counts() + df.team2.value_counts())) * 100
    
    # if (win_prcntage.)
    
    win_prcntage = pd.DataFrame({
        'Team_Name': [team_1, team_2],
        'Win %age': [win_prcntage.get(team_1), win_prcntage.get(team_2)]
    })

    fig = px.pie(win_prcntage, names='Team_Name',
                    values='Win %age', hole=0.3,
                    color="Team_Name",
                    color_discrete_map={team_1: "#e84393",
                                        team_2: "#434343"})
    return fig


def team_in_most_season(team_1, team_2, cleaner_obj, season_ls):
    df = cleaner_obj.new_df
    df = df.loc[df["season"].isin(season_ls)]

    series_1 = df.loc[df["team1"] == team_1].season.value_counts()
    series_2 = df.loc[df["team1"] == team_2].season.value_counts()

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

    fig = px.histogram(df, x='Season',
                        y='Match Count', 
                        color="Team_name",
                        barmode="group", 
                        color_discrete_map={team_1: "#55efc4",
                                            team_2: "#e84393"})

    return fig

def player_match_season(team_1, team_2, cleaner_obj, season_ls):
    df = cleaner_obj.new_df
    df = df.loc[df["season"].isin(season_ls)]

    series_1 = df.loc[df["team1"] == team_1].player_of_match.value_counts()[:5]
    series_2 = df.loc[df["team1"] == team_2].player_of_match.value_counts()[:5]

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

    fig = px.histogram(df, x='Player Name',
                        y='Match Count', 
                        color="Team_name",
                        barmode="group", 
                        color_discrete_map={team_1: "#55efc4",
                                            team_2: "#e84393"})

    return fig

def win_visu_by_toss(team_name, cleaner_obj, season_ls):
    df = cleaner_obj.new_df
    df = df.loc[df["season"].isin(season_ls)]
    
    # Getting all the data if `team_name` wins the toss.
    field_data = df[(df["toss_winner"] == team_name) & (df["toss_decision"] == "field")]
    bat_data = df[(df["toss_winner"] == team_name) & (df["toss_decision"] == "bat")]

    winning_field_data = len(field_data[field_data["winner"] == team_name])
    winning_bat_data = len(bat_data[bat_data["winner"] == team_name])
    
    # Winning percentage based on fielding decision
    win_field = (winning_field_data/ max(len(field_data), 1)) * 100
    
    # Winning percentage based on batting decision
    win_bat = (winning_bat_data/ max(len(bat_data), 1)) * 100
    
    # Creating dataframe for plot
    data = [['Fielding', win_field], ['Batting', win_bat]]
    data = pd.DataFrame (data,columns=['Decision','Win_%age'])
    
    fig = px.pie(data, values='Win_%age', names='Decision', title=team_name, hole=0.3, color="Decision", color_discrete_map={"Batting": "#e84393", "Fielding": "#434343"})
    return fig

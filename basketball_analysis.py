# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 12:17:17 2020
@author: mayureshm
When tried using the original excel data file it returned a NULL data type
hence made a smaller sampled sized dataframe manually
s
Reference: https://github.com/ixarchakos/nba-games
(In this NBA games 2015-16 were worked upon)
"""

import pandas as pd
Basket_ball = {
        "home_team" : ['ATL', 'CHI', 'GS', 'ORL', 'BOS', 'BKN', 'DET', 'MIA', \
                       'TOR', 'HOU', 'MEM', 'MIL', 'OKC', 'PHX', 'POR', 'SAC',\
                       'LAL', 'IND', 'NY', 'LAC'],
        "away_team" : ['DET', 'CLE', 'NO', 'WSH', 'PHI', 'CHI', 'UTAH', 'CHA',\
                       'IND', 'DEN', 'CLE', 'NY', 'SA', 'DAL', 'NO', 'LAC', \
                       'MIN', 'MEM', 'ATL', 'DAL'],
        "home_points" : [94, 97, 111, 87, 112, 100, 92, 104, 106, 85, 76, 97, \
                         112, 95, 112, 104, 111, 103, 101, 104],
        "away_points" : [106, 95, 95, 88, 95, 115, 87, 94, 99, 105, 106, 122,\
                         106, 111, 94, 111, 112, 112, 112, 88],
        "field_gp_home" : [45.1, 42.5, 42.7, 37, 45.9, 41.9, 40.5, 49.3, 45, \
                           34.5, 35.4, 34.9, 48.8, 39.1, 50, 43.6, 38.9, 47.4,\
                           40.9, 43.7],
        "field_gp_away" : [38.5, 40.4, 42.2, 39.3, 41.0, 53.8, 46.7, 39.3, \
                           37.2, 50.6, 48.8, 45.2, 48.4, 7.1, 39.6, 52.5,\
                           45.8, 50, 50.6, 36.1],
        "threeper_home" : [29.6, 36.8, 30.0, 19.2, 33.3, 0.0, 36.8, 60.0,\
                           38.9, 22.9, 12.5, 50.0, 36.8, 25, 37.5, 45.8, \
                           26.5, 40.0, 20.7, 25.8],
        "threeper_away" : [41.4, 31, 33.3, 25, 31.8, 50, 16.7, 25, 39.1, \
                           48.1, 44.8, 39.1, 33.3, 47.6, 33.3, 31.6, 25, \
                           43.8, 41.7, 20],
        "rebound_home" : [44, 58, 64, 68, 49, 50, 52, 47, 67, 53, 47, 57, 52,\
                          65, 56, 59, 61, 46, 57, 68],
        "rebound_away" : [69, 62, 49, 60, 50, 49, 47, 49, 48, 58, 61, 59, 43,\
                          55, 52, 49, 48, 49, 49, 59],
        "assists_away" : [23, 26, 21, 17, 12, 20, 15, 16, 23, 26, 29, 24, 22,\
                          24, 19, 20, 24, 26, 26, 22],
        "assists_home" : [22, 13, 29, 20, 31, 19, 16, 23, 19, 17, 15, 17, 21,\
                          15, 22, 24, 18, 23, 21, 21],
        "turnovers_home" : [15, 13, 20, 16, 17, 13, 12, 13, 21, 17, 16, 18,\
                            19, 18, 12, 18, 14, 20, 21, 8],
        "turnovers_away" : [15, 11, 19, 18, 24, 20, 12, 9, 13, 21, 19, 11,\
                            13, 8, 11, 15, 8, 14, 16, 13],
        }

df = pd.DataFrame(Basket_ball)
print(df)

key_1 = input("Enter the home team:")
key2 = input("Enter the away team:")
key3 = int(input("Enter the lower range for assists:"))#Lower range for home\
#assists function and type casting is done
key4 = int(input("Enter the higher range for assists:"))#Upper range for home\
#assists function and typecasting is done
key5 = int(input("Enter the lower num _arr range:"))
key6 = int(input("Enter the upper num_arr range:"))
def findhometeammatches():#Visible that NBA finalists have little home game\
#in first 20 NBA games in NBA 2015-16
    af1 = df[df.home_team == (key_1)]
    print(af1)
def findawayteammatches():
    af2 = df[df.away_team == (key2)]
    print(af2)
def hometeampoints():
    af3 = df[df['home_points'] >= 100]
    l1 = len(af3)
    print(af3)
    print("Number of home teams having greater than 100 point games are :", l1)    
def awayteampoints():
    af4 = df[df['away_points'] >= 100]
    l2 = len(af4)
    print(af4)
    print("The number of away teams having greater than 100 point games are :", l2)
"""
Out of the total we see 12 out of 20 times home team has scored > 100
Out of the total away matches 11 out of 200 times team has scored > 100 
Hence we can conclude that there is no significant home or away advantage in NBA.
"""

v = df.min()                      #Find minimum of all the non string values

def meanhometeam(b):
    b = df.mean()      #Mean is calculated for all the non string data columns
    af5 = b['home_points']
    print("The mean home team points are ", af5)        
def number_of_assists_for_homeinrange():#Number of assists i.e. passes\
#leading to baskets have been calculated for a range
    z = df[df.assists_home > key3]
    w = z[z.assists_home < key4]
    print("The team details for those teams lying in this assists range are: ")
    print(w)
def minturnoversaway():#Turnover here refers to granting possession of the \
#ball to the oppsition
    af6 = min(df['turnovers_away'])
    print("THe minimum turnovers by an away team are: ", af6)
    af7 = df[df['turnovers_away'] == af6]
    print("Details of the away team giving minimum turnovers: ", af7)
"""
Here it is interesting to note that away teams that have lesser turnovers have gone on to win the match as illustrated in this case 
"""
u = df.to_numpy()
print(u)
def returnnumberbasedonrowandcolumn(): 
    if key5 in range(0, 21):
        if key6 in range(0, 16):
            o = (u[key5, key6])
            print(o)
        else:
            print("Out of bounds indexing:")
    else:
        print("Out of bounds indexing:")
""" 
Another method of accessing elements of the dataframe but out of bounds accessing is not cleared mentioned
h=df.iloc[key5,key6]                   
print(h)
""" 
df = df.assign(Home_Team_Status=['L', 'W', 'L', 'W', 'L', 'W', 'L', 'W', 'L',\
                     'W', 'L', 'W', 'L', 'W', 'L', 'W', 'L', 'W', 'L', 'W'])
def findpointsdifferential(df):
    df = df.assign(pointsdiff=(df.home_points)-(df.away_points))
    print(df)
def sortbyreboundaway(df):
    df = df.sort_values(by='rebound_away')     
    print(df)

#If we see the aboove function we understand that rebounds have cost teams games.
#More rebounds translates to better possibility of winning the match.
#Rebound in basketball is to try and gain ball possession once it is hits\
#the rim or board

def plotbasedongoalp(df):
    df.plot(x='home_team', y=['threeper_home', 'field_gp_home'])
#This plot shoes us that field goal or non 3 point shooting percentage is quite common.
#It is the 3 point percentage that matters at times and may decide a win or a loss
def writetoexcel():
    df.to_excel('output.xlsx', sheet_name='Sheet1')
findhometeammatches()
findawayteammatches()
hometeampoints()
awayteampoints()
meanhometeam(df)
number_of_assists_for_homeinrange()
minturnoversaway()
returnnumberbasedonrowandcolumn()
findpointsdifferential(df)
sortbyreboundaway(df)
plotbasedongoalp(df)
writetoexcel()
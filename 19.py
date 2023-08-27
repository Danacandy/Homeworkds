import numpy as np


a_zeros = np.zeros((4, 3))
b_ones = np.ones((4, 3))
c_range = np.arange(12).reshape(4, 3)

print("a. All zeros array:\n", a_zeros)
print("b. All ones array:\n", b_ones)
print("c. Numbers from 0 to 11 array:\n", c_range)

# b. Tabulate F(x) = 2x^2 + 5
x_values = np.arange(1, 101, 1)
f_values = 2 * x_values ** 2 + 5

print("b. Tabulated F(x) = 2x^2 + 5:")
for x, f in zip(x_values, f_values):
    print(f"F({x}) = {f}")

# c. Tabulate F(x) = e^(-x)
x_values = np.arange(-10, 11, 1)
f_values = np.exp(-x_values)

print("c. Tabulated F(x) = e^(-x):")
for x, f in zip(x_values, f_values):
    print(f"F({x}) = {f}")


import pandas as pd
from io import StringIO


data = """Team,Goals,Shots on target,Shots off target,Shooting Accuracy,% Goals-to-shots,Total shots (inc. Blocked),Hit Woodwork,Penalty goals,Penalties not scored,Headed goals,Passes,Passes completed,Passing Accuracy,Touches,Crosses,Dribbles,Corners Taken,Tackles,Clearances,Interceptions,Clearances off line,Clean Sheets,Blocks,Goals conceded,Saves made,Saves-to-shots ratio,Fouls Won,Fouls Conceded,Offsides,Yellow Cards,Red Cards,Subs on,Subs off,Players Used
Croatia,4,13,12,51.9%,16.0%,32,0,0,0,2,1076,828,76.9%,1706,60,42,14,49,83,56,,0,10,3,13,81.3%,41,62,2,9,0,9,9,16
Czech Republic,4,13,18,41.9%,12.9%,39,0,0,0,0,1565,1223,78.1%,2358,46,68,21,62,98,37,2,1,10,6,9,60.1%,53,73,8,7,0,11,11,19
Denmark,4,10,10,50.0%,20.0%,27,1,0,0,3,1298,1082,83.3%,1873,43,32,16,40,61,59,0,1,10,5,10,66.7%,25,38,8,4,0,7,7,15
England,5,11,18,50.0%,17.2%,40,0,0,0,3,1488,1200,80.6%,2440,58,60,16,86,106,72,1,2,29,3,22,88.1%,43,45,6,5,0,11,11,16
France,3,22,24,37.9%,6.5%,65,1,0,0,0,2066,1803,87.2%,2909,55,76,28,71,76,58,0,1,7,5,6,54.6%,36,51,5,6,0,11,11,19
Germany,10,32,32,47.8%,15.6%,80,2,1,0,2,2774,2427,87.4%,3761,101,60,35,91,73,69,0,1,11,6,10,62.6%,63,49,12,4,0,15,15,17
Greece,5,8,18,30.7%,19.2%,32,1,1,1,0,1187,911,76.7%,2016,52,53,10,65,123,87,0,1,23,7,13,65.1%,67,48,12,9,1,12,12,20
Italy,6,34,45,43.0%,7.5%,110,2,0,0,2,3016,2531,83.9%,4363,75,75,30,98,137,136,1,2,18,7,20,74.1%,101,89,16,16,0,18,18,19
Netherlands,2,12,36,25.0%,4.1%,60,2,0,0,0,1556,1381,88.7%,2163,50,49,22,34,41,41,0,0,9,5,12,70.6%,35,30,3,5,0,7,7,15
Poland,2,15,23,39.4%,5.2%,48,0,0,0,1,1059,852,80.4%,1724,55,39,14,67,87,62,0,0,8,3,6,66.7%,48,56,3,7,1,7,7,17
Portugal,6,22,42,34.3%,9.3%,82,6,0,0,2,1891,1461,77.2%,2958,91,64,41,78,92,86,0,2,11,4,10,71.5%,73,90,10,12,0,14,14,16
Republic of Ireland,1,7,12,36.8%,5.2%,28,0,0,0,1,851,606,71.2%,1433,43,18,8,45,78,43,1,0,23,9,17,65.4%,43,51,11,6,1,10,10,17
Russia,5,9,31,22.5%,12.5%,"""


df = pd.read_csv(StringIO(data))


selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]

print(selected_columns)


num_teams = df['Team'].nunique()
print("Number of teams participated in Euro2012:", num_teams)


high_scoring_teams = df[df['Goals'] > 6]
print("Teams that scored more than 6 goals:")
print(high_scoring_teams)





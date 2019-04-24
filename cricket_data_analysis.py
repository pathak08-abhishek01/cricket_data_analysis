import yaml

# Read the data of the format .yaml type
with open('file.yaml', 'r') as f:
    cricdata = yaml.safe_load(f)

# Find data type of the file
print(type(cricdata))

# In which city, and at which venue the match was played and where was it played ?
city = cricdata['info']['city']
venue = cricdata['info']['venue']
print('Match was played in {} at {}'.format(city, venue))

# Which are all the teams that played in the tournament ? How many teams participated in total?
teams = cricdata['info']['teams']
no_of_teams = len(teams)
print('{} teams played the match viz {} and {}'.format(no_of_teams, teams[0], teams[1]))

# Which team won the toss and what was the decision of toss winner ?
toss_winner = cricdata['info']['toss']['winner']
toss_decision = cricdata['info']['toss']['decision']
print('{} won the toss and choose to {}'.format(toss_winner, toss_decision))

# Find the first bowler and first batsman who played the first ball of the first inning
batsman = cricdata['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
bowler = cricdata['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
print('1st Ball was bowled by {} and played by {}'.format(bowler, batsman))

# How many deliveries were delivered in first inning ?
no_of_balls_1st = len(cricdata['innings'][0]['1st innings']['deliveries'])
print('{} balls were delivered in the 1st innings'.format(no_of_balls_1st))
# How many deliveries were delivered in second inning ?
no_of_balls_2nd = len(cricdata['innings'][1]['2nd innings']['deliveries'])
print('{} balls were delivered in the 2nd innings'.format(no_of_balls_2nd))
# Which team won and how ?
winner = cricdata['info']['outcome']['winner']
wintype = cricdata['info']['outcome']['by']
for x, y in wintype.items():
    by = x
    runs = y
print('{} won the Match by {} {}'.format(winner, runs, by))
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
import numpy as np

# Load the datasets
print("Datasets")
ucl_stats = pd.read_csv('ucl_stats.csv')
player_stats = pd.read_csv('UEFA_CL_Player_stats.csv')


# Check for missing values
print("Missing values")
print(ucl_stats.isnull().sum())
print(player_stats.isnull().sum())

# Handle missing values (example: replace with mean)
print("Handle missing values")
ucl_stats['goals_scored'].fillna(ucl_stats['goals_scored'].mean(), inplace=True)
ucl_stats['goals_conceded'].fillna(ucl_stats['goals_conceded'].mean(), inplace=True)


# Convert data types if needed
print("Converting datatypes")
ucl_stats['year'] = pd.to_numeric(ucl_stats['year'], errors='coerce')
ucl_stats['match_played'] = pd.to_numeric(ucl_stats['match_played'], errors='coerce')
ucl_stats['wins'] = pd.to_numeric(ucl_stats['wins'], errors='coerce')
ucl_stats['draws'] = pd.to_numeric(ucl_stats['draws'], errors='coerce')
ucl_stats['losts'] = pd.to_numeric(ucl_stats['losts'], errors='coerce')
ucl_stats['goals_scored'] = pd.to_numeric(ucl_stats['goals_scored'], errors='coerce')
ucl_stats['goals_conceded'] = pd.to_numeric(ucl_stats['goals_conceded'], errors='coerce')
ucl_stats['gd'] = pd.to_numeric(ucl_stats['gd'], errors='coerce')
ucl_stats['group_point'] = pd.to_numeric(ucl_stats['group_point'], errors='coerce')
ucl_stats['champions'] = pd.to_numeric(ucl_stats['champions'], errors='coerce')

print("Columns of datasets")
print(ucl_stats.columns)

# Basic exploratory data analysis
print("Head of the dataset:")
print(ucl_stats.head())

print("\nSummary statistics of the dataset:")
print(ucl_stats.describe())

# Analyze the distribution of variables
print("\nDistribution of 'goals_scored' variable:")
print(ucl_stats['goals_scored'].value_counts())

# Calculate summary statistics
print("Summary statistics")
goals_scored = ucl_stats['goals_scored']
match_played = ucl_stats['match_played']
wins = ucl_stats['wins']
draws = ucl_stats['draws']
losts = ucl_stats['losts']

print("\nSummary statistics of 'goals_scored' variable:")
print("Mean:", goals_scored.mean())
print("Median:", goals_scored.median())
print("Maximum:", goals_scored.max())
print("Minimum:", goals_scored.min())

print("\nSummary statistics of 'match_played' variable:")
print("Mean:", match_played.mean())
print("Median:", match_played.median())
print("Maximum:", match_played.max())
print("Minimum:", match_played.min())

print("\nSummary statistics of 'wins' variable:")
print("Mean:", wins.mean())
print("Median:", wins.median())
print("Maximum:", wins.max())
print("Minimum:", wins.min())

print("\nSummary statistics of 'draws' variable:")
print("Mean:", draws.mean())
print("Median:", draws.median())
print("Maximum:", draws.max())
print("Minimum:", draws.min())

print("\nSummary statistics of 'losts' variable:")
print("Mean:", losts.mean())
print("Median:", losts.median())
print("Maximum:", losts.max())
print("Minimum:", losts.min())





#Visualisation



# Bar chart - Distribution of teams --- Top 10 Teams in Champions League, 10 most appearing teams in the dataset , ekipet me te paraqitura qe jane permendur me shpesh
team_counts = ucl_stats['team'].value_counts().head(10)
plt.figure(figsize=(10, 10))
ax = sns.barplot(x=team_counts.index, y=team_counts.values)
plt.xlabel('Team')
plt.ylabel('Count')
plt.title('Top 10 Teams in Champions League')
plt.xticks(rotation=45)
plt.show()
#1



# Line plot - Trend of goals scored over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='year', y='goals_scored', data=ucl_stats)
plt.xlabel('Year')
plt.ylabel('Goals Scored')
plt.title('Trend of Goals Scored in Champions League over Time')
plt.show()
#2





# Scatter plot - Relationship between goals scored and goals conceded
plt.figure(figsize=(8, 6))
sns.scatterplot(x='goals_scored', y='goals_conceded', data=ucl_stats)
plt.xlabel('Goals Scored')
plt.ylabel('Goals Conceded')
plt.title('Relationship between Goals Scored and Goals Conceded')
plt.show()
#3




# Box plot - Comparison of goals scored across teams, i selekton 5 random teams edhe i shpreh golat ne perqindje
random_teams = random.sample(list(ucl_stats['team'].unique()), k=5)
selected_teams_stats = ucl_stats[ucl_stats['team'].isin(random_teams)]
total_goals_scored = selected_teams_stats.groupby('team')['goals_scored'].sum()
plt.figure(figsize=(8, 8))
plt.pie(total_goals_scored, labels=total_goals_scored.index, autopct='%1.1f%%', startangle=90)
plt.title('Goals Scored by 5 Random Teams')
plt.axis('equal')
plt.show()
#4





# Analyze team performance
team_performance = ucl_stats.groupby('team').agg({'goals_scored': 'sum', 'wins': 'sum', 'losts': 'sum'}).reset_index()
team_performance = team_performance.sort_values('goals_scored', ascending=False)
# Create a ranking of teams based on goals scored
team_performance['rank'] = team_performance['goals_scored'].rank(ascending=False)

#Kodi i mesiperm nuk shfaq asgje ne console ne ekzekutim te menjehershem, vetem na sherben per analize te metutjeshme





# Plot line chart - Performance of a specific team over multiple seasons
team_name = 'Real Madrid'
team_stats = ucl_stats[ucl_stats['team'] == team_name]
plt.figure(figsize=(10, 6))
sns.lineplot(x='year', y='goals_scored', data=team_stats)
plt.xlabel('Year')
plt.ylabel('Goals Scored')
plt.title(f'Goals Scored by {team_name} in Champions League')
plt.show()
#5




#goals by 10 random teams
import random
# Select 10 random teams
random_teams = random.sample(list(team_performance['team']), k=10)
# Filter the data for the selected teams
selected_teams_performance = team_performance[team_performance['team'].isin(random_teams)]
# Plot the bar chart for the selected teams
plt.figure(figsize=(12, 6))
sns.barplot(x='team', y='goals_scored', data=selected_teams_performance)
plt.xlabel('Team')
plt.ylabel('Total Goals Scored')
plt.title('Total Goals Scored by 10 Random Teams')
plt.xticks(rotation=45)
plt.show()
#6





#import numpy as np
# Generate random colors for each data point
colors = np.random.rand(len(team_performance))
plt.figure(figsize=(8, 6))
plt.scatter(x='wins', y='goals_scored', data=team_performance, c=colors, cmap='viridis', s=80)
plt.xlabel('Total Wins')
plt.ylabel('Total Goals Scored')
plt.title('Relationship between Wins and Goals Scored')
# Add a grid
plt.grid(True, linestyle='dotted', linewidth=0.8, alpha=0.3)
# Add a background pattern
plt.gca().set_facecolor('#222222')
# Customize tick labels and axes color
plt.xticks(color='white')
plt.yticks(color='white')
plt.gca().spines['bottom'].set_color('white')
plt.gca().spines['left'].set_color('white')
plt.show()
#7


import random
# Select 4 random teams
random_teams = random.sample(list(team_performance['team']), k=4)
# Filter the data for the selected teams
selected_teams_performance = team_performance[team_performance['team'].isin(random_teams)].copy()
# Calculate the percentage of goals scored for each team
total_goals_scored = selected_teams_performance['goals_scored'].sum()
selected_teams_performance.loc[:, 'goals_percentage'] = selected_teams_performance['goals_scored'] / total_goals_scored * 100
# Sort the teams based on the goals scored percentage
selected_teams_performance = selected_teams_performance.sort_values('goals_percentage', ascending=False)
# Create a horizontal pie chart
plt.figure(figsize=(8, 6))
colors = ['#FF6347', '#FFA500', '#FFFF00', '#32CD32', '#4169E1', '#9370DB']
explode = [0.1] * len(selected_teams_performance)  # Explode the slices for emphasis
plt.pie(selected_teams_performance['goals_percentage'], labels=selected_teams_performance['team'], explode=explode, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Goals Scored by 4 Random Teams')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
#8



#Line plot - Comparison of goals scored by top-ranked teams:
# Calculate the rank based on goals scored
team_performance['rank'] = team_performance['goals_scored'].rank(ascending=False)
# Select the top 5 teams
top_teams = team_performance[team_performance['rank'] <= 5]
# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='goals_scored', y='team', data=top_teams, palette='Blues_d')
plt.xlabel('Goals Scored')
plt.ylabel('Team')
plt.title('Top 5 Teams in Goals Scored')
plt.show()
#9


#Stacked Bar chart - Distribution of Wins, Draws, and Losses:
plt.figure(figsize=(10, 6))
ucl_stats[['wins', 'draws', 'losts']].sum().plot(kind='bar', stacked=True)
plt.xlabel('Result')
plt.ylabel('Count')
plt.title('Distribution of Wins, Draws, and Losses')
plt.show()
#10

#Line plot - Trend of Goals Scored and Conceded over Time:
plt.figure(figsize=(10, 6))
sns.lineplot(x='year', y='goals_scored', data=ucl_stats, label='Goals Scored')
sns.lineplot(x='year', y='goals_conceded', data=ucl_stats, label='Goals Conceded')
plt.xlabel('Year')
plt.ylabel('Goals')
plt.title('Trend of Goals Scored and Conceded over Time')
plt.legend()
plt.show()
#11

#Bar chart - Top 10 Teams with the Highest Goal Difference:
plt.figure(figsize=(10, 6))
top_goal_diff = ucl_stats.groupby('team')['gd'].sum().nlargest(10)
sns.barplot(x=top_goal_diff.index, y=top_goal_diff.values)
plt.xlabel('Team')
plt.ylabel('Goal Difference')
plt.title('Top 10 Teams with the Highest Goal Difference')
plt.xticks(rotation=45)
plt.show()
#12

#Scatter plot - Relationship between Goals Scored and Group Points:
plt.figure(figsize=(8, 6))
sns.scatterplot(x='goals_scored', y='group_point', data=ucl_stats)
plt.xlabel('Goals Scored')
plt.ylabel('Group Points')
plt.title('Relationship between Goals Scored and Group Points')
plt.show()
#13


# STATISTICS ONLY FOR UCL PLAYERS
player_stats = pd.read_csv('UEFA_CL_Player_stats.csv')
#shfaqja e kolonave ne console
print(player_stats.columns)
print(player_stats.columns)

#Top 10 Goal Scorers in Champions League
top_goal_scorers = player_stats.groupby('name')['goals'].sum().nlargest(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_goal_scorers.index, y=top_goal_scorers.values)
plt.xlabel('Player')
plt.ylabel('Total Goals')
plt.title('Top 10 Goal Scorers')
plt.xticks(rotation=45)
plt.show()
#14

#Bar Chart - Top 10 Assist Providers:
# Compute top assist providers
top_assist_providers = player_stats.groupby('name')['assists'].sum().nlargest(10)
# Set custom color palette
colors = sns.color_palette('viridis', len(top_assist_providers))
# Plot the bar chart with custom styling
plt.figure(figsize=(10, 6))
sns.barplot(x=top_assist_providers.index, y=top_assist_providers.values, palette=colors)
# Add labels and title with custom styling
plt.xlabel('Player', fontsize=12, fontweight='bold')
plt.ylabel('Total Assists', fontsize=12, fontweight='bold')
plt.title('Top 10 Assist Providers', fontsize=14, fontweight='bold')
# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
# Remove y-axis ticks
plt.yticks([])
# Add data labels on top of each bar
for i, value in enumerate(top_assist_providers.values):
    plt.text(i, value, str(value), ha='center', va='bottom', fontsize=10, fontweight='bold')
# Remove spines (borders) around the plot
sns.despine()
# Show the plot
plt.show()
#15

#Histogram - Distribution of Player Ratings:
# Set the figure size and style
plt.figure(figsize=(10, 6))
sns.set(style='whitegrid')
# Plot the histogram with density curve
sns.histplot(player_stats['rating'], bins=88, kde=True)
# Customize the plot
plt.xlabel('Rating', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Distribution of Player Ratings', fontsize=14, fontweight='bold')
# Add vertical lines for mean and median
mean_rating = player_stats['rating'].mean()
median_rating = player_stats['rating'].median()
plt.axvline(mean_rating, color='red', linestyle='--', label='Mean')
plt.axvline(median_rating, color='blue', linestyle='--', label='Median')
# Add a legend
plt.legend()
# Remove spines (borders) around the plot
sns.despine()
# Show the plot
plt.show()
#16

#Area Chart - Player Performance across Seasons:
selected_player = 'Lionel Messi'
player_performance = player_stats[player_stats['name'] == selected_player]
plt.figure(figsize=(10, 6))
sns.lineplot(x='season', y='goals', data=player_performance, color='red', label='Goals')
sns.lineplot(x='season', y='assists', data=player_performance, color='blue', label='Assists')
plt.fill_between(player_performance['season'], player_performance['goals'], player_performance['assists'], color='orange', alpha=0.5)
plt.xlabel('Season')
plt.ylabel('Count')
plt.title(f'Player Performance across Seasons for {selected_player}')
plt.xticks(rotation=45)
plt.legend()
plt.show()
#17

#Scatter Plot - Goals vs Assists
plt.figure(figsize=(8, 6))
sns.scatterplot(x='goals', y='assists', data=player_stats)
plt.xlabel('Goals')
plt.ylabel('Assists')
plt.title('Goals vs. Assists')
plt.show()
#18

#Correlation Matrix - Player Statistics:
player_stats_subset = player_stats[['goals', 'assists', 'yellowRedCards', 'rating']]
correlation_matrix = player_stats_subset.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix - Player Statistics')
plt.show()
#19



#The graph for goals from 8 random players in random season
import random
# Select a random season
random_season = random.choice(player_stats['season'].unique())
# Filter the data for the selected season
player_stats_season = player_stats[player_stats['season'] == random_season]
# Select 8 random players
random_players = random.sample(list(player_stats_season['name'].unique()), 8)
# Filter the data for the selected players
player_stats_selected = player_stats_season[player_stats_season['name'].isin(random_players)]
# Group the data by player and calculate the total number of goals
goals_by_player = player_stats_selected.groupby('name')['goals'].sum()
if not goals_by_player.empty:
    # Sort the players based on the number of goals in descending order
    goals_by_player = goals_by_player.sort_values(ascending=False)
    # Create a bar graph to visualize the number of goals
    plt.figure(figsize=(11, 13))
    goals_by_player.plot(kind='bar')
    plt.xlabel('Player')
    plt.ylabel('Number of Goals')
    plt.title(f'Number of Goals by Players in {random_season}')
    plt.xticks(rotation=45)
    plt.show()
else:
    print(f"No data available for the season: {random_season}")
#20









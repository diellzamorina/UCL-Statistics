
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
player_stats = pd.read_csv('UEFA_CL_Player_stats.csv')
import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
player_stats = pd.read_csv('UEFA_CL_Player_stats.csv')
# Assuming you have a DataFrame called player_stats with columns 'name', 'season', and 'goals'
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










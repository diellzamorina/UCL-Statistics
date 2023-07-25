# Bar chart - Distribution of teams --- Top 10 Teams in Champions League, 10 most appearing teams in the dataset , ekipet me te paraqitura qe jane permendur me shpesh

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
ucl_stats = pd.read_csv('ucl_stats.csv')
# Bar chart - Distribution of teams --- Top 10 Teams in Champions League, 10 most appearing teams in the dataset , ekipet me te paraqitura qe jane permendur me shpesh
team_counts = ucl_stats['team'].value_counts().head(10)
plt.figure(figsize=(10, 10))
ax = sns.barplot(x=team_counts.index, y=team_counts.values)
plt.xlabel('Team')
plt.ylabel('Count')
plt.title('Top 10 Teams in Champions League')
plt.xticks(rotation=45)
plt.show()



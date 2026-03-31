# Question: Ranking System

import pandas as pd

scores = [88, 92, 79, 93, 85]
players = ['P1','P2','P3','P4','P5']

s = pd.Series(scores, index=players)

# Ranking
rank = s.rank(ascending=False)

# Top 3
top3 = s.sort_values(ascending=False).head(3)

# Lowest
lowest = s.idxmin()

print(rank)
print(top3)
print("Lowest:", lowest)

# Output:
# Rankings of players
# Top 3 players
# Player with lowest score
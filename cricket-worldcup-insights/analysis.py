import pandas as pd
import matplotlib.pyplot as plt

# World Cup match data (sample)
data = {
    "Team": ["India", "Australia", "England", "India", "Australia", "India"],
    "Opponent": ["Australia", "England", "India", "England", "India", "Australia"],
    "Runs_Scored": [250, 270, 230, 280, 260, 300],
    "Wickets_Lost": [8, 7, 9, 6, 8, 5],
    "Result": ["Win", "Win", "Loss", "Win", "Loss", "Win"]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Total matches per team
matches_per_team = df["Team"].value_counts()
print("\nMatches per team:")
print(matches_per_team)

# Average runs scored by each team
avg_runs = df.groupby("Team")["Runs_Scored"].mean()
print("\nAverage runs scored:")
print(avg_runs)

# Win percentage per team
win_percentage = (
    df[df["Result"] == "Win"]["Team"].value_counts()
    / df["Team"].value_counts()
) * 100

print("\nWin percentage:")
print(win_percentage)

avg_runs.plot(kind="bar", title="Average Runs by Team")
plt.ylabel("Runs")
plt.xlabel("Team")
plt.tight_layout()
plt.show()

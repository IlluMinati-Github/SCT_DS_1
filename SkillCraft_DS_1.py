import pandas as pd

# Load the population dataset
df = pd.read_csv(r"C:\Users\Dell\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_787209\API_SP.POP.TOTL_DS2_en_csv_v2_787209.csv", skiprows=4)
print(df.head())

india = df[df["Country Name"] == "India"]
population_2022 = india["2022"].values[0]
print("India Population in 2022:", population_2022)

# Pick year
year = "2022"

# Sort top 10 countries by population
top10 = df[["Country Name", year]].sort_values(by=year, ascending=False).head(10)

# Plot
import matplotlib.pyplot as plt

plt.bar(top10["Country Name"], top10[year] / 1e6, color="skyblue")
plt.xticks(rotation=45)
plt.title(f"Top 10 Countries by Population in {year}")
plt.ylabel("Population (millions)")
plt.show()

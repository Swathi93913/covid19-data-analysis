import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Covid_project\covid_19_data.csv.csv")

# Show first rows
print(data.head())

# Convert date column
data['Date'] = pd.to_datetime(data['Date'])

# Group by date
daily_cases = data.groupby('Date')['Confirmed'].sum()

# Plot graph
plt.figure(figsize=(10,5))
plt.plot(daily_cases)

plt.title("Daily COVID-19 Confirmed Cases")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")

plt.show()

# Death trend
daily_deaths = data.groupby('Date')['Deaths'].sum()

plt.figure(figsize=(10,5))
plt.plot(daily_deaths)

plt.title("Daily COVID-19 Deaths")
plt.xlabel("Date")
plt.ylabel("Deaths")

plt.show()

# Recovery trend
daily_recovery = data.groupby('Date')['Cured'].sum()

plt.figure(figsize=(10,5))
plt.plot(daily_recovery)

plt.title("Daily COVID-19 Recovery Trend")
plt.xlabel("Date")
plt.ylabel("Recovered")

plt.show()

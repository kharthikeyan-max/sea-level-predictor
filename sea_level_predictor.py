import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
# Read data from CSV file
df = pd.read_csv("epa-sea-level.csv")

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(
    df["Year"],
    df["CSIRO Adjusted Sea Level"],
    label="Observed data"
)

# Linear regression using all available data
slope, intercept, r_value, p_value, std_err = linregress(
    df["Year"],
    df["CSIRO Adjusted Sea Level"]
)

# Create years from the first year through 2050
years = pd.Series(range(df["Year"].min(), 2051))

# Calculate predicted sea levels
predicted_sea_level = slope * years + intercept

# Plot line of best fit
plt.plot(
    years,
    predicted_sea_level,
    color="red",
    label="Line of best fit (1880-2014)"
)

# Filter data from year 2000 onward
recent_data = df[df["Year"] >= 2000]

# Linear regression using data from 2000 onward
slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(
    recent_data["Year"],
    recent_data["CSIRO Adjusted Sea Level"]
)

# Create years from 2000 through 2050
recent_years = pd.Series(range(2000, 2051))

# Calculate predicted sea levels using the 2000+ trend
predicted_recent_sea_level = (
    slope_2000 * recent_years + intercept_2000
)

# Plot second line of best fit
plt.plot(
    recent_years,
    predicted_recent_sea_level,
    color="green",
    label="Line of best fit (2000 onward)"
)

# Labels and title
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")

# Add legend
plt.legend()

# Save and return plot
plt.savefig("sea_level_plot.png")

return plt.gca()

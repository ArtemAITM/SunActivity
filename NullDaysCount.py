import pandas as pd
import matplotlib.pyplot as plt

file_path = "data.csv"
data = pd.read_csv(file_path, delimiter=';', header=None)

data.columns = ['year', 'month', 'day', 'decimal_year', 'column_4', 'column_5', 'column_6', 'column_7']

filtered_data = data[data['column_4'] == 0]

days_per_year = filtered_data.groupby('year').size()
filtered_years = days_per_year[days_per_year >= 50]

all_years = range(1815, 2026, 5)

plt.figure(figsize=(12, 6))
plt.bar(filtered_years.index, filtered_years, color='skyblue', edgecolor='black')

plt.xticks(
    ticks=all_years,
    labels=all_years,
    rotation=30, fontsize=10
)

plt.title("Количество безупречных дней по годам", fontsize=14)
plt.xlabel("Год", fontsize=12)
plt.ylabel("Количество дней", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = 'data.csv'
data = pd.read_csv(file_path, delimiter=';', header=None)

data.columns = ['Year', 'Month', 'Day', 'Decimal_Year', 'Value_1', 'Value_2', 'Value_3', 'Flag']
filtered_data = data[data['Value_1'] != -1]
output_dir = "dayDataForYears"
os.makedirs(output_dir, exist_ok=True)

unique_years = filtered_data['Year'].unique()

for year in unique_years:
    year_data = filtered_data[filtered_data['Year'] == year].copy()
    year_data.loc[:, 'Day_of_Year'] = (year_data['Month'] - 1) * 30 + year_data['Day']
    plt.figure(figsize=(12, 6))
    plt.scatter(year_data['Day_of_Year'], year_data['Value_1'], s=10, label=f'{year}', alpha=0.7)
    plt.title(f'График значений по дням в {year} году')
    plt.xlabel('День года')
    plt.ylabel('Значение (пятый столбец)')
    plt.grid(True)
    plt.legend()
    output_path = os.path.join(output_dir, f"{year}.jpg")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

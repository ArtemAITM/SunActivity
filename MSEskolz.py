import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data.csv'
data = pd.read_csv(file_path, delimiter=';', header=None)
data.columns = ['Year', 'Month', 'Day', 'Decimal_Year', 'Value_2', 'dsfdgs', 'Value_3', 'Flag']
filtered_data = data[data['Value_2'] != -1]
annual_mean = filtered_data.groupby('Year')['Value_2'].mean()
print(annual_mean)
window = 5
rolling_mean = annual_mean.rolling(window=window, center=True).mean()

threshold = 35
anomalies = annual_mean[abs(annual_mean - rolling_mean) > threshold]

plt.figure(figsize=(12, 6))
plt.plot(annual_mean.index, annual_mean.values, label='Среднегодовые значения', marker='o')
plt.plot(rolling_mean.index, rolling_mean.values, label='Скользящее среднее', linestyle='--')
plt.scatter(anomalies.index, anomalies.values, color='red', label='Аномалии', zorder=5)
plt.xticks(ticks=range(1820, 2026, 5), rotation=45)

plt.title('Анализ среднегодовых значений и аномалий')
plt.xlabel('Год')
plt.ylabel('Значение')
plt.legend()
plt.grid(True)
plt.show()

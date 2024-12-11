import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

data = pd.read_csv('SN_d_tot_V2.0.csv', delimiter=";")


def create_sequences(data, input_days, predict_days):
    xs, ys = [], []
    for i in range(len(data) - input_days - predict_days + 1):
        x = data[i:i + input_days]
        y = data[i + input_days:i + input_days + predict_days]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)


input_days = 21
predict_days = 1
x_data, y_data = create_sequences(data, input_days, predict_days)
total_samples = len(x_data)
train_size = int(total_samples * 0.8)
x_train, y_train = x_data[:train_size], y_data[:train_size]
x_test, y_test = x_data[train_size:], y_data[train_size:]

model = Sequential([
    LSTM(1, input_shape=(21, 8), return_sequences=False),
    Dense(64),
    Dense(1)
])
model.compile(optimizer='adam', loss='mean_squared_error')
epochs = 5
batch_size = 4

history = model.fit(
    x_train,
    y_train,
    epochs=epochs,
    batch_size=batch_size,
    validation_data=(x_test, y_test),
    verbose=1
)

predictions = model.predict(x_test)
print("Прогноз на неделю вперед:")
print(predictions)
model.save("model.h5")
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

file = open("testModel.txt", "r")
scaler = MinMaxScaler()
test = np.array([int(i) for i in file.readline().split(";")])
scaled_data = scaler.fit_transform(test.reshape(-1, 1))

test = np.expand_dims(test, axis=1)
print(scaled_data, test.shape)
model = tf.keras.models.load_model("model.h5")
predictions = model.predict(test)
predictions = scaler.inverse_transform(predictions)
print(predictions[0])
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

#dataset
X = []
y = []

for i in range(1, 9):
    X.append([i, i+1, i+2])
    y.append(i+3)

X = np.array(X)
y = np.array(y)
#

X = X.reshape((X.shape[0], X.shape[1], 1))


model = Sequential([
    LSTM(32, activation='relu', input_shape=(3, 1)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=200, verbose=0)

test_input = np.array([[9, 10, 11]]).reshape((1, 3, 1))
pred = model.predict(test_input, verbose=0)
print(f"Entrada: [9, 10, 11] → Predicción: {pred[0][0]:.2f}")

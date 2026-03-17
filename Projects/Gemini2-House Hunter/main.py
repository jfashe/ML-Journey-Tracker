# project_2_houses.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. GENERATE DATA
# Let's pretend we have 100 houses. X = Square Footage, y = Price
np.random.seed(42) # Keeps the "random" numbers the same every time you run it
sq_ft = 2000 * np.random.rand(100, 1)
prices = 50 * sq_ft + (10000 + np.random.randn(100, 1) * 5000) # Added some "noise" (randomness)

# 2. THE SPLIT (Crucial for Interviews!)
# We hide some data (test) from the AI so we can quiz it later.
# 80% to learn, 20% to test.
X_train, X_test, y_train, y_test = train_test_split(sq_ft, prices, test_size=0.2)

# 3. TRAIN
model = LinearRegression()
model.fit(X_train, y_train)

# 4. EVALUATE (The Quiz)
# We ask the AI to guess prices for houses it has NEVER seen (X_test)
predictions = model.predict(X_test)

# How far off were we on average? 
error = mean_squared_error(y_test, predictions)
print(f"Model Error (MSE): {error:.2f}")

# 5. PLOT
plt.scatter(X_test, y_test, color='black', label='Actual')
plt.plot(X_test, predictions, color='green', linewidth=3, label='Prediction')
plt.legend()
plt.show()
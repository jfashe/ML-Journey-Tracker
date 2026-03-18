# Machine Learning 102
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1 - Generate data bruddaman
# 100 houses, x = sqft, y = price
np.random.seed(42)
sq_ft = 2000 * np.random.rand(100,1)
price = 50 * sq_ft + (10000 + np.random.randn(100,1) * 5000) # Remains consistent (50 times sqft for price) with added noise (or randomness)

# 2 - The Split (Crucial)
# This is where we hide some darta from the AI, in order to quiz it later. 80% to learn  with, 20% for testing. Aka, "80/20" split. The 20% is unseen by the model (during training).
x_train, x_test, y_train, y_test = train_test_split(sq_ft, price, test_size = 0.2)

# 3 - Train
model = LinearRegression()
model.fit(x_train, y_train)

# 4 - Evaluate (Quiz)
# Asking the AI to guess prices it for houses that it hasn't seen (x_test, the other .8)
predictions = model.predict(x_test)

# 5 - Results
error = mean_squared_error(y_test, predictions)
print(f"Model Error (mse): {error:.2f}")

# 6 - Plot
plt.scatter(x_test,y_test, color = 'black', label = 'Actual')
plt.plot(x_test,predictions, color='green', linewidth=3, label='Prediction')
plt.legend()
plt.show()
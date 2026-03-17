# project_1_lemonade.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# STEP 1: Create our "Experience" (Data)
# 'X' is the cause (Temperature), 'y' is the result (Lemonade Sales)
# We use .reshape(-1, 1) because the AI expects a list of lists, not a flat list.
temperature = np.array([60, 65, 70, 75, 80, 85, 90]).reshape(-1, 1)
sales = np.array([50, 70, 90, 110, 130, 150, 170])

# STEP 2: Pick a "Brain" (The Model)
# LinearRegression just means "drawing a straight line through dots"
model = LinearRegression()

# STEP 3: Study (Training)
# This is where the AI looks at the numbers and finds the pattern
model.fit(temperature, sales)

# STEP 4: Make a Guess (Prediction)
# Let's see how much we'd make if it was 95 degrees
predict_temp = np.array([[95]])
prediction = model.predict(predict_temp)

print(f"If it's 95 degrees, we will likely make ${prediction[0]:.2f}")

# STEP 5: Visualize (Matplotlib)
plt.scatter(temperature, sales, color='blue') # Plot the actual dots
plt.plot(temperature, model.predict(temperature), color='red') # Plot the AI's "line"
plt.title('Temperature vs Lemonade Sales')
plt.xlabel('Temp')
plt.ylabel('Sales')
plt.show()
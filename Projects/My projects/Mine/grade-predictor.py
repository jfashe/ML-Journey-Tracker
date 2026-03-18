# Machine Learning 101
import numpy as np # 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print("We good?")

# Creating data
# Grades (hours of studying vs #grade)
hours = np.array([0,2,3,5,10,22,15,24,4,18]).reshape(-1,1)
grade = np.array([50,68,72,75,88,100,90,96,80,96])#.reshape(-1,1)

# Picking a model (linear regression ofc)
model = LinearRegression()

# Training model
model.fit(hours,grade)

# Prediction (Magic)
predict_grade = np.array([[8]]) # Mess around with this number. Guesses what grade will be received (target) from x amount of hours spent studying (feature)
prediction = model.predict(predict_grade)

# Print pseudo, prediction[0] bc numpy arrays are zero-indexed
print(f"If you spend 8 hours studying, you'll likely get a grade of {prediction[0]:.2f}%")

# Visualize using matplotlib
plt.scatter(hours,grade)
plt.plot(hours,grade, color='red') # Creates scatterplot of data
plt.title('Hours vs Grade Earned')
plt.xlabel('Hours Studying')
plt.ylabel('Sales')
plt.show()
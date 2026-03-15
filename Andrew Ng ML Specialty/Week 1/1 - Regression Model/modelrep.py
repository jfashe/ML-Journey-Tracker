import numpy as np
import matplotlib.pyplot as plt
plt.style.use('./deeplearning.mplstyle')

def clear():
    print("------------------------------")
def follow():
    print("-----")

# x_train is the input variable (size in 1000 square feet)
# y_train is the target (price in 1000s of dollars)
x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")
clear()

# .shape returns the number of training examples as a tuple
print(f"x_train.shape: {x_train.shape}")
m = x_train.shape[0]        #.shape[0] returns just the first value in the tuple (actual # of training examples)
print(f"Number of training examples is: {m}")
clear()


"""
as said in the notebook, we can use the len() func aswell
print(f"Number of training examples is: {len(x_train)}")
clear()
"""

# Training example:
i = 0

x_i = x_train[i]
y_i = y_train[i]

# x^i or y^i is the ith example (not 1--1st, i--ith)
print(f"x^({i}), y^({i}) = ({x_i}, {y_i})") # despite being denoted as an exponent (^i), it is not an exponent.
clear()


# Plotting data points:
#plt.scatter(x_train, y_train, marker = 'x', c = 'r')
#plt.title("Housing prices")
#plt.ylabel('Price (in 1000s of dollars)')   #y - axis
#plt.xlabel('Size (1000sqft)')               #x - axis
#plt.show()

# Model Function
w = 200
b = 100
print(f"w: {w}")
print(f"b: {b}")

# value of function f_w,b (x^(i)) for two data points
f_wb = w * x_train[0] + b     #for x^(0)
f_wb = w * x_train[1] + b     #for x^(1)

def computer_model_output(x, w, b):
    """
    Computes the prediction of a linear model
    Args:
        x (ndarray (m,)): Data, m examles
        w,b (scalar)    : model parameters
    Returns
        f_wb (ndarray (m,)): model prediction
    """
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b

    return f_wb

tmp_f_wb = computer_model_output(x_train,w,b)

# Plot model prediction
plt.plot(x_train, tmp_f_wb, c='b', label="Our Prediction")

#  data points
plt.scatter(x_train, y_train, marker="x", c="r", label="Actual Values")

plt.title("Housing Prices")
plt.xlabel("Price (in 1000s of dollars)")
plt.ylabel("Size (1000 sqft)")
plt.legend()
plt.show()

x_i = 1.2
cost_1200sqft = w * x_i + b

print(f"${cost_1200sqft:.0f} thousand dollars")
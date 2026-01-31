import numpy as np
import matplotlib.pyplot as plt
plt.style.use('./deeplearning.mplstyle')

def clear():
    print("------------------------------")
def follow():
    print("-----")


x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")
clear()

print(f"x_train.shape: {x_train.shape}")
m = x_train.shape[0]
print(f"Number of training examples is: {m}")
clear()

i = 0

x_i = x_train[i]
y_i = y_train[i]

print(f"x^({i}), y^({i}) = ({x_i}, {y_i})")

plt.scatter(x_train, y_train, marker = 'x', c = 'r')
plt.title("Housing prices")
plt.ylabel('Price (in 1000s of dollars)')
plt.xlabel('Size (1000sqft)')
plt.show()

w = 200
b = 100
print(f"w: {w}")
print(f"b: {b}")

f_wb = w * x_train[0] + b
f_wb = w * x_train[1] + b

def computer_model_output(x, w, b):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b

    return f_wb

tmp_f_wb = computer_model_output(x_train,w,b)

plt.plot(x_train, tmp_f_wb, c='b', label="Our Prediction")

plt.scatter(x_train, y_train, marker="x", c="r", label="Actual Values")

plt.title("Housing Prices")
plt.xlabel("Price (in 1000s of dollars)")
plt.ylabel("Size (1000 sqft)")
plt.legend()
plt.show()

x_i = 1.2
cost_1200sqft = w * x_i + b

print(f"${cost_1200sqft:.0f} thousand dollars")
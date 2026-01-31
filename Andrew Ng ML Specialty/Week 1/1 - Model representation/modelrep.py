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
follow()

#as said in the notebook, we can use the len() func aswell
print(f"Number of training examples is: {len(x_train)}")
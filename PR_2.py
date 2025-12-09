import numpy as np
import matplotlib.pyplot as plt

# Simple dataset (x -> y)
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 4, 2, 4, 5])

# 1. Calculate slope (m) and intercept (b)
n = len(x)

sum_x = np.sum(x)
sum_y = np.sum(y)

sum_xy = np.sum(x * y)
sum_x2 = np.sum(x * x)

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b = (sum_y - m * sum_x) / n

print("Slope (m):", m)
print("Intercept (b):", b)

# 2. Make predictions
y_pred = m * x + b

# 3. Plot regression line
plt.scatter(x, y, color='blue', label='Actual Points')
plt.plot(x, y_pred, color='red', label='Regression Line')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression (Using Arrays)")
plt.legend()
plt.show()

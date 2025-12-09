import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

# Load sklearn diabetes dataset
diabetes = load_diabetes()

# Convert to DataFrame
data = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
data['target'] = diabetes.target

# Features and target
X = data.drop('target', axis=1)
y = data['target']

# Train model
model = LinearRegression()
model.fit(X, y)

# -------------------------------------------
# Fix other features at their mean values
# -------------------------------------------
means = X.mean()

# We vary only one feature: BMI
bmi_range = np.linspace(X['bmi'].min(), X['bmi'].max(), 50)

# We will create three predictive lines for:
# Low BP, Medium BP, High BP
bp_low = X['bp'].quantile(0.25)
bp_mid = X['bp'].quantile(0.50)
bp_high = X['bp'].quantile(0.75)

# Predictive line 1 - low BP
X_line_low = means.copy()
X_line_low['bp'] = bp_low
X_line_low = pd.DataFrame([X_line_low] * len(bmi_range))
X_line_low['bmi'] = bmi_range
y_low = model.predict(X_line_low)

# Predictive line 2 - mid BP
X_line_mid = means.copy()
X_line_mid['bp'] = bp_mid
X_line_mid = pd.DataFrame([X_line_mid] * len(bmi_range))
X_line_mid['bmi'] = bmi_range
y_mid = model.predict(X_line_mid)

# Predictive line 3 - high BP
X_line_high = means.copy()
X_line_high['bp'] = bp_high
X_line_high = pd.DataFrame([X_line_high] * len(bmi_range))
X_line_high['bmi'] = bmi_range
y_high = model.predict(X_line_high)

# -------------------------------------------
# Plotting
# -------------------------------------------
plt.scatter(X['bmi'], y, color="gray", alpha=0.5, label="Actual Data")

plt.plot(bmi_range, y_low, color="red", label="Low BP (25th percentile)")
plt.plot(bmi_range, y_mid, color="blue", label="Mid BP (50th percentile)")
plt.plot(bmi_range, y_high, color="green", label="High BP (75th percentile)")

plt.xlabel("BMI")
plt.ylabel("Disease Progression")
plt.title("Multiple Linear Regression — Three Predictive Lines")
plt.legend()
plt.show()
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import statsmodels.api as sm

from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression

# Load AirPassengers dataset from statsmodels
data = sm.datasets.get_rdataset("AirPassengers").data

# Prepare DataFrame: Select only the 'value' column
df = pd.DataFrame(data['value'])

# Create date column
df['date'] = pd.date_range(start='1949-01', periods=len(df), freq='ME') # Changed 'M' to 'ME'

# Set date as index
df = df.set_index('date')

# Prepare data for regression (convert dates to ordinal numbers)
X = np.array(df.index.map(datetime.toordinal)).reshape(-1,1)
y = df['value'].values

# Train-test split (80% train, 20% test)
split = int(len(X)*0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Create and train Linear Regression model (sklearn)
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation metrics
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Custom Accuracy (within ±10%)
tolerance = 0.1 * y_test
accuracy = np.mean(np.abs(y_test - y_pred) <= tolerance)

# Print results
print("R² Score:", r2)
print("Mean Squared Error:", mse)
print("Accuracy (within 10% tolerance):", accuracy)

# Plot actual vs predicted
plt.figure(figsize=(10,6))
plt.plot(df.index[split:], y_test, label='Actual', color='blue')
plt.plot(df.index[split:], y_pred, label='Predicted', linestyle='--', color='red')
plt.xlabel('Date')
plt.ylabel('Passengers')
plt.title('AirPassengers Prediction vs Actual')
plt.legend()
plt.grid(True)
plt.show()
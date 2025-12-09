# ridge_regression_sklearn_example.py
# Requires: scikit-learn, pandas, numpy, matplotlib
# pip install scikit-learn pandas numpy matplotlib

import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 1) Load dataset
data = load_diabetes()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

# 2) Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3) Scale features (important for regularization)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4) Hyperparameter search for alpha (regularization strength)
param_grid = {'alpha': np.logspace(-3, 3, 50)}   # try many alphas from 1e-3 to 1e3
ridge = Ridge(random_state=42, max_iter=10000)
grid = GridSearchCV(ridge, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid.fit(X_train_scaled, y_train)

best_alpha = grid.best_params_['alpha']
cv_mse_mean = -grid.best_score_

# 5) Evaluate best estimator on test set
best_ridge = grid.best_estimator_
y_pred = best_ridge.predict(X_test_scaled)
test_mse = mean_squared_error(y_test, y_pred)
test_r2 = r2_score(y_test, y_pred)

# 6) Coefficients (map back to feature names)
coeffs = pd.Series(best_ridge.coef_, index=X.columns).sort_values(key=abs, ascending=False)

# 7) Print summary
print("=== Ridge Regression Summary ===")
print(f"Best alpha (from GridSearchCV): {best_alpha}")
print(f"Cross-validated MSE (train, mean): {cv_mse_mean:.4f}")
print(f"Test MSE: {test_mse:.4f}")
print(f"Test R^2: {test_r2:.4f}")
print("\nTop coefficients (by absolute value):")
print(coeffs.head(10).to_string())

# 8) Plot Actual vs Predicted
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], linestyle='--')
plt.xlabel("Actual target")
plt.ylabel("Predicted target")
plt.title("Ridge Regression: Actual vs Predicted")
plt.tight_layout()
plt.show()

# 9) Plot coefficients
plt.figure(figsize=(8,4))
coeffs.plot(kind='bar')
plt.ylabel("Coefficient value")
plt.title("Ridge Regression Coefficients (sorted by absolute value)")
plt.tight_layout()
plt.show()

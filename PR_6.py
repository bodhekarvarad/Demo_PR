# lasso_regression_sklearn_example.py
# Requires: scikit-learn, pandas, numpy, matplotlib
# pip install scikit-learn pandas numpy matplotlib

import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso, LassoCV
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# ---------- Load data ----------
data = load_diabetes()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

# ---------- Train/test split ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------- Scale features (important for L1 regularization) ----------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---------------------------
# Approach A: GridSearchCV
# ---------------------------
param_grid = {'alpha': np.logspace(-4, 1, 50)}  # try many alphas from 1e-4 to 10
lasso = Lasso(random_state=42, max_iter=10000)
grid = GridSearchCV(lasso, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid.fit(X_train_scaled, y_train)

best_alpha_grid = grid.best_params_['alpha']
cv_mse_grid = -grid.best_score_
best_lasso_grid = grid.best_estimator_

y_pred_grid = best_lasso_grid.predict(X_test_scaled)
test_mse_grid = mean_squared_error(y_test, y_pred_grid)
test_r2_grid = r2_score(y_test, y_pred_grid)

coeffs_grid = pd.Series(best_lasso_grid.coef_, index=X.columns).sort_values(key=abs, ascending=False)

# Print GridSearch results
print("=== Lasso (GridSearchCV) ===")
print(f"Best alpha: {best_alpha_grid}")
print(f"Cross-validated MSE (train, mean): {cv_mse_grid:.4f}")
print(f"Test MSE: {test_mse_grid:.4f}")
print(f"Test R^2: {test_r2_grid:.4f}")
print("\nNonzero coefficients (GridSearch):")
print(coeffs_grid[coeffs_grid != 0].to_string())

# ---------------------------
# Approach B: LassoCV (recommended)
# ---------------------------
# LassoCV chooses alpha via internal CV. Use a wide grid of alphas.
alphas_cv = np.logspace(-4, 1, 100)
lasso_cv = LassoCV(alphas=alphas_cv, cv=5, random_state=42, max_iter=10000)
lasso_cv.fit(X_train_scaled, y_train)

best_alpha_cv = lasso_cv.alpha_
# LassoCV doesn't return neg_mean_squared_error directly; evaluate by cross_val_score if needed.
y_pred_cv = lasso_cv.predict(X_test_scaled)
test_mse_cv = mean_squared_error(y_test, y_pred_cv)
test_r2_cv = r2_score(y_test, y_pred_cv)
coeffs_cv = pd.Series(lasso_cv.coef_, index=X.columns).sort_values(key=abs, ascending=False)

print("\n=== LassoCV ===")
print(f"Chosen alpha (LassoCV): {best_alpha_cv:.6g}")
print(f"Test MSE: {test_mse_cv:.4f}")
print(f"Test R^2: {test_r2_cv:.4f}")
print("\nNonzero coefficients (LassoCV):")
print(coeffs_cv[coeffs_cv != 0].to_string())

# ---------- Plots ----------
# 1) Actual vs Predicted (LassoCV)
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred_cv)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], linestyle='--')
plt.xlabel("Actual target")
plt.ylabel("Predicted target (LassoCV)")
plt.title("Lasso Regression: Actual vs Predicted (LassoCV)")
plt.tight_layout()
plt.show()


# ---------- Optional: Save model ----------
# import joblib
# joblib.dump({'model': lasso_cv, 'scaler': scaler}, "lasso_model_and_scaler.pkl")

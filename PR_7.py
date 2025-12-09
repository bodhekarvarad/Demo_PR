# dt_classifier_example.py
# pip install scikit-learn pandas numpy matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load iris
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Base model + hyperparameter tuning
param_grid = {
    'max_depth': [None, 2, 3, 4, 5, 6, 8],
    'min_samples_split': [2, 3, 4, 6],
    'min_samples_leaf': [1, 1, 2, 3]
}
dt = DecisionTreeClassifier(random_state=42)
grid = GridSearchCV(dt, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid.fit(X_train, y_train)

best_dt = grid.best_estimator_
print("Best params:", grid.best_params_)

# Evaluate
y_pred = best_dt.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Test accuracy: {acc:.4f}")
print("\nClassification report:\n", classification_report(y_test, y_pred, target_names=data.target_names))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))

# Print textual tree
print("\nTextual representation of the tree:")
print(export_text(best_dt, feature_names=list(X.columns)))

# Plot tree
plt.figure(figsize=(10,6))
plot_tree(best_dt, feature_names=X.columns, class_names=data.target_names, filled=True, rounded=True)
plt.title("Decision Tree (Iris) — Best estimator")
plt.show()

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# Load clean dataset (NO CSV needed)
data = load_breast_cancer()
# Features and target
X = data.data
y = data.target
# Convert to DataFrame (optional, for understanding)
df = pd.DataFrame(X, columns=data.feature_names)
df['target'] = y
print("Dataset shape:", df.shape)
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Model
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Results
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Plot
plt.scatter(y_test, y_pred_proba)
plt.xlabel("Actual (0 = Malignant, 1 = Benign)")
plt.ylabel("Predicted Probability")
plt.title("Breast Cancer Prediction (Clean Dataset)")
plt.show()
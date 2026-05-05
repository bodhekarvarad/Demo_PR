# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, \
    mean_squared_error, r2_score
# ✅ Load dataset from URL (no file error)
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Fare'] = df['Fare'].fillna(df['Fare'].median())
# Select features
X = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
# One-hot encoding
X = pd.get_dummies(X, drop_first=True)
# Target
y = df['Survived']
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.25, random_state=42
)
# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# Train KNN model
model_knn = KNeighborsClassifier(n_neighbors=5)
model_knn.fit(X_train, y_train)
# Predictions
y_pred = model_knn.predict(X_test)
# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)
# Heatmap
plt.figure(figsize=(5,5))
sn.heatmap(cm, annot=True, cmap="Blues", fmt="d")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title("Confusion Matrix Heatmap")
plt.show()
# Classification Report
print("Classification Report:\n", classification_report(y_test, y_pred))
# MSE
print("MSE:", mean_squared_error(y_test, y_pred))
# R² Score
print("R² Score:", r2_score(y_test, y_pred))
# Graph
plt.figure(figsize=(6,4))
plt.scatter(range(len(y_test)), y_test, label='Actual')
plt.scatter(range(len(y_pred)), y_pred, marker='x', label='Predicted')
plt.xlabel("Sample Index")
plt.ylabel("Survival (0=No, 1=Yes)")
plt.title("Actual vs Predicted Survival (KNN)")
plt.legend()
plt.show()
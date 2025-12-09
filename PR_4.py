from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# -------------------------
# Load sklearn dataset
# -------------------------
data = load_breast_cancer()
X = data.data[:, :2]    # Use only 2 features for visualization (mean radius, mean texture)
y = data.target

df = pd.DataFrame(X, columns=["mean_radius", "mean_texture"])
df["target"] = y
print("First few rows:\n", df.head())

# -------------------------
# Train/test split
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# -------------------------
# Feature scaling
# -------------------------
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# -------------------------
# Logistic Regression Model
# -------------------------
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# -------------------------
# Predictions & Metrics
# -------------------------
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)

print("\nConfusion Matrix:\n", cm)
print("\nAccuracy:", acc)

# -------------------------
# Decision Boundary Plot
# -------------------------
def plot_boundary(X_set, y_set, title):
    X1, X2 = np.meshgrid(
        np.arange(X_set[:,0].min() - 1, X_set[:,0].max() + 1, 0.01),
        np.arange(X_set[:,1].min() - 1, X_set[:,1].max() + 1, 0.01),
    )

    plt.contourf(
        X1, X2,
        classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
        alpha=0.5,
        cmap=ListedColormap(("red", "green"))
    )

    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(
            X_set[y_set == j, 0],
            X_set[y_set == j, 1],
            c=ListedColormap(("red", "green"))(i),
            label=str(j)
        )

    plt.title(title)
    plt.xlabel("mean_radius")
    plt.ylabel("mean_texture")
    plt.legend()
    plt.show()


# Plot training and test sets
plot_boundary(X_train, y_train, "Logistic Regression (Training Set)")
plot_boundary(X_test, y_test, "Logistic Regression (Test Set)")

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler

# 1. Load ONE dataset (Iris)
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print("Dataset Head:")
print(df.head())

# 2. Data Handling (cleaning)
df = df.drop_duplicates()       # remove duplicates
df = df.fillna(df.mean())       # handle missing values (iris has none, but good practice)

# Separate features & target
X = df.drop('target', axis=1)

# 3. Apply MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

print("\nScaled Data (Head):")
print(scaled_df.head())

# 4. Graph: Before vs After Scaling for a single feature
feature = "sepal length (cm)"

plt.figure(figsize=(12,5))

# original
plt.subplot(1,2,1)
plt.hist(X[feature], bins=20)
plt.title("Original Data\n" + feature)
plt.xlabel("Value")
plt.ylabel("Frequency")

# scaled
plt.subplot(1,2,2)
plt.hist(scaled_df[feature], bins=20)
plt.title("Scaled Data (MinMaxScaler)\n" + feature)
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

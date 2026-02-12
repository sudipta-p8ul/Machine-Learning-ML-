# CART Classification using scikit-learn
# Dataset: Income, LawnSize -> Decision (Owner / Nonowner)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix

# -------------------------------------------------
# 1. Create Dataset
# -------------------------------------------------
data = {
    "Income": [60, 75, 85.5, 52.8, 64.8, 64.8, 61.5, 43.2, 87, 84,
               110.1, 49.2, 108, 74.4, 82.8, 66, 69, 47.4, 93, 33,
               51, 51, 81, 63],
    "LawnSize": [18.4, 19.6, 16.8, 20.8, 21.6, 17.2, 20.8, 20.4, 23.6, 17.6,
                 19.2, 17.6, 17.6, 20.4, 22.4, 18.4, 20, 16.4, 20.8, 18.8,
                 22, 14, 20, 14.8],
    "Decision": ["Owner", "Nonowner", "Owner", "Nonowner", "Owner", "Nonowner",
                 "Owner", "Nonowner", "Owner", "Nonowner", "Owner", "Nonowner",
                 "Owner", "Nonowner", "Owner", "Nonowner", "Owner", "Nonowner",
                 "Owner", "Nonowner", "Owner", "Nonowner", "Owner", "Nonowner"]
}

df = pd.DataFrame(data)

# -------------------------------------------------
# 2. Encode Target Variable
# -------------------------------------------------
le = LabelEncoder()
df["Decision"] = le.fit_transform(df["Decision"])
# Owner = 1, Nonowner = 0

# -------------------------------------------------
# 3. Split Features and Target
# -------------------------------------------------
X = df[["Income", "LawnSize"]]
y = df["Decision"]

# -------------------------------------------------
# 4. Train-Test Split
# -------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# -------------------------------------------------
# 5. Create CART Model (Gini Index)
# -------------------------------------------------
cart_model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

# -------------------------------------------------
# 6. Train Model
# -------------------------------------------------
cart_model.fit(X_train, y_train)

# -------------------------------------------------
# 7. Prediction & Accuracy
# -------------------------------------------------
y_pred = cart_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("CART Classification Accuracy:", accuracy)

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# -------------------------------------------------
# 8. Visualize CART Tree
# -------------------------------------------------
plt.figure(figsize=(14, 6))
plot_tree(
    cart_model,
    feature_names=["Income", "LawnSize"],
    class_names=["Nonowner", "Owner"],
    filled=True
)
plt.title("CART Decision Tree (Owner vs Nonowner)")
plt.show()

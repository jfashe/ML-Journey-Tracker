# project_3_spam_filter.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report

# 1. GENERATE SYNTHETIC DATA
# Imagine 200 emails. 
# Features: [Length of email, Number of exclamation marks]
np.random.seed(42)
X = np.random.rand(200, 2) * 100 
# Target: 1 if Spam, 0 if Not Spam
# We create a fake rule: If length + exclamation marks > 100, it's likely spam
y = (X[:, 0] + X[:, 1] > 100).astype(int)

# 2. SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# 3. FEATURE SCALING (Standardization)
# INTERVIEW TIP: Models like Logistic Regression hate it when one number is 
# 0.001 and another is 1000. Scaling makes them all live in the same "range."
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. TRAIN THE CLASSIFIER
# Even though it says "Regression" in the name, Logistic Regression is for CATEGORIES.
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# 5. PREDICT & EVALUATE
predictions = model.predict(X_test_scaled)

# The Confusion Matrix shows: [True Negatives, False Positives]
#                             [False Negatives, True Positives]
print("--- Confusion Matrix ---")
print(confusion_matrix(y_test, predictions))
print("\n--- Detailed Report ---")
print(classification_report(y_test, predictions))

# 6. VISUALIZE THE "DECISION BOUNDARY"
# This shows the line the AI drew to separate Spam from Not Spam
plt.scatter(X_test_scaled[:, 0], X_test_scaled[:, 1], c=predictions, cmap='bwr', alpha=0.7)
plt.title("Spam vs Not Spam (Standardized Scales)")
plt.xlabel("Email Length")
plt.ylabel("Exclamation Marks")
plt.show()
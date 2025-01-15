import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Define the Support Vector Machine (SVM) class
class SVM:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.w = None
        self.b = None

    # Train the SVM
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)  # Initialize weights
        self.b = 0  # Initialize bias

        # Ensure labels are -1 and 1
        y = np.where(y <= 0, -1, 1)

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                condition = y[idx] * (np.dot(x_i, self.w) + self.b) >= 1
                if condition:
                    self.w -= self.lr * (2 * self.w)
                else:
                    self.w -= self.lr * (2 * self.w - np.dot(x_i, y[idx]))
                    self.b -= self.lr * y[idx]

    # Predict using the trained SVM
    def predict(self, X):
        prediction = np.dot(X, self.w) + self.b
        return np.sign(prediction).astype(int)

# Load and preprocess data
data = pd.read_csv('PatientDetails_Classification.csv')
data = data.drop('Patient Name', axis=1)  # Drop non-relevant column

# Separate features and target
X = data.drop(columns='TARGET').values
y = data['TARGET'].values

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the SVM model
clf = SVM()
clf.fit(X_train, y_train)

# Make predictions
predictions = clf.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy}')

# Confusion matrix
cm = confusion_matrix(y_test, predictions)
tp, fp, fn, tn = cm[0][0], cm[0][1], cm[1][0], cm[1][1]

# Print confusion matrix elements
print(f"True Positives (TP): {tp}")
print(f"False Positives (FP): {fp}")
print(f"False Negatives (FN): {fn}")
print(f"True Negatives (TN): {tn}")

# Recalculate accuracy from confusion matrix
accuracy_from_cm = (tp + tn) / (tp + fp + fn + tn)
print(f'Accuracy from confusion matrix: {accuracy_from_cm}')

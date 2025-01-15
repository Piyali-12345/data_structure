import pandas as pd
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Load data
data = pd.read_csv('diabetes.csv')

# Preview data
print(data.head())

# Split features and labels
X = data.drop(columns='Outcome').values
y = data['Outcome'].values

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2)**2))

# Function to implement K-Nearest Neighbors algorithm
def knn_predict(X_train, y_train, X_test, k):
    pred = []
    for test_point in X_test:
        distances = [euclidean_distance(train_point, test_point) for train_point in X_train]
        nearest_indices = np.argsort(distances)[:k]
        nearest_labels = y_train[nearest_indices]
        # Use majority voting to determine the predicted label
        mejvoting = Counter(nearest_labels).most_common(1)[0][0]
        pred.append(mejvoting)
    return np.array(pred)

# Make predictions using k=7
y_pred = knn_predict(X_train, y_train, X_test, k=7)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Confusion matrix and metrics
cm = confusion_matrix(y_test, y_pred)
tp = cm[0][0]  # True Positives
fp = cm[0][1]  # False Positives
fn = cm[1][0]  # False Negatives
tn = cm[1][1]  # True Negatives

print(f"True Positives: {tp}")
print(f"False Positives: {fp}")
print(f"False Negatives: {fn}")
print(f"True Negatives: {tn}")

# Recalculate accuracy from confusion matrix
accuracy_from_cm = (tp + tn) / (tp + fp + fn + tn)
print(f'Accuracy from confusion matrix: {accuracy_from_cm}')

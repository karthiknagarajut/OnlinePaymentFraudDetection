# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import xgboost as xgb
import pickle
from scipy import stats

# Load data
df = pd.read_csv("new_file.csv")

# Data cleaning
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.dropna()

# Remove outliers
num = [var for var in df.columns if df[var].dtype != 'O' and var != 'isFraud']
for x in num:
    bmi_z_score = stats.zscore(df[x])
    df = df[np.abs(bmi_z_score) <= 3]

# Label encoding for 'type'
le = LabelEncoder()
df['type'] = le.fit_transform(df['type'])

# Save LabelEncoder for prediction
pickle.dump(le, open("label_encoder.pkl", "wb"))

# Split data into features and target
x = df.drop("isFraud", axis=1)
y = df["isFraud"]

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=0.2)

# Train XGBoost Classifier
xgb1 = xgb.XGBClassifier()
xgb1.fit(x_train, y_train)

# Evaluate model
y_test_predict = xgb1.predict(x_test)
test_accuracy = accuracy_score(y_test, y_test_predict)
train_accuracy = accuracy_score(y_train, xgb1.predict(x_train))
print("Train Accuracy:", train_accuracy)
print("Test Accuracy:", test_accuracy)

# Classification Report
print(classification_report(y_test, y_test_predict))

# Save the model
pickle.dump(xgb1, open("model.pkl", "wb"))

print("Model and Label Encoder saved successfully!")

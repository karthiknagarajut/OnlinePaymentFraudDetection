# 🏦 Online Payment Fraud Detection System

![Fraud Detection](https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Online_Payment_Icon.svg/1200px-Online_Payment_Icon.svg.png)

## 🚀 Overview
This project is an **Online Payment Fraud Detection System** that utilizes machine learning to detect fraudulent transactions. The model analyzes transaction details and predicts whether a transaction is fraudulent or legitimate.

🔍 **Live Demo:** [Online Payment Fraud Detection](https://onlinepaymentfrauddetectionbykarthiknagaraju.streamlit.app/)

## 📥 Dataset
- Source: [Kaggle - Online Payments Fraud Detection Dataset](https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset)
- Size: 6,362,620 transactions

## ⚙️ Data Processing
1. Removed unnecessary columns: `isFlaggedFraud`, `nameOrig`, and `nameDest`.
2. Cleaned missing values.
3. Removed outliers using Z-score.
4. Encoded categorical features using `LabelEncoder`.

## 📊 Models and Accuracy
- **Random Forest Classifier**:
  - Train Accuracy: 99.88%
  - Test Accuracy: 99.86%
- **Decision Tree**:
  - Train Accuracy: 99.76%
  - Test Accuracy: 99.72%
- **SVM**:
  - Train Accuracy: 98.34%
  - Test Accuracy: 98.20%
- **XGBoost (Selected Model)**:
  - Train Accuracy: **99.947%**
  - Test Accuracy: **99.948%**

## 🏗️ Tech Stack
- Python
- Pandas
- Scikit-learn
- XGBoost
- Streamlit

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/karthiknagarajut/OnlinePaymentFraudDetection.git
   cd OnlinePaymentFraudDetection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## 📌 How to Use
1. Enter the transaction details:
   - Step
   - Transaction Type
   - Amount
   - Old Balance Origin
   - New Balance Origin
   - Old Balance Destination
   - New Balance Destination
2. Click on the **Predict** button to check if the transaction is fraudulent.
3. Use the **Reset** button to clear inputs.

## 🧠 Results
- **Precision:** 0.80
- **Recall:** 0.65
- **F1-Score:** 0.72

## 💻 Author
- **THOTA KARTHIK NAGA RAJU**

## 🌟 Acknowledgments
- Kaggle for providing the dataset.
- Streamlit for the interactive UI.

---
🚀 *Empowering Safe Transactions with Machine Learning!* 🌐


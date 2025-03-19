import streamlit as st
import pandas as pd
import pickle

# Load the model and label encoder
model = pickle.load(open('model.pkl', 'rb'))
le = pickle.load(open('label_encoder.pkl', 'rb'))

# Center-align content with custom CSS
st.markdown("""
    <style>
        .center-text {text-align: center;}
        .button-container {display: flex; justify-content: space-between; margin-top: 20px;}
        .input-container {display: flex; justify-content: space-between; align-items: center;}
        .button-row {display: flex; justify-content: space-between; align-items: center; margin-top: 40px;}
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<h1 class="center-text">🔍 Online Payment Fraud Detection System</h1>', unsafe_allow_html=True)
st.markdown('<p class="center-text">💬 This project uses machine learning to detect fraudulent transactions in online payments. It analyzes transaction details and predicts whether a transaction is fraudulent or not.</p>', unsafe_allow_html=True)

# Initialize session state for reset and prediction result
if 'result' not in st.session_state:
    st.session_state.result = None

# Input fields
step = st.number_input('📅 Step', min_value=0, value=int(0 if 'reset' in st.session_state else st.session_state.get('step', 0)))
transaction_type = st.selectbox('🔁 Transaction Type', le.classes_, index=0 if 'reset' in st.session_state else st.session_state.get('transaction_type_index', 0))
amount = st.number_input('💸 Amount', min_value=0.0, value=float(0.0 if 'reset' in st.session_state else st.session_state.get('amount', 0.0)))
oldbalanceOrg = st.number_input('🏦 Old Balance Origin', min_value=0.0, value=float(0.0 if 'reset' in st.session_state else st.session_state.get('oldbalanceOrg', 0.0)))
newbalanceOrig = st.number_input('🏦 New Balance Origin', min_value=0.0, value=float(0.0 if 'reset' in st.session_state else st.session_state.get('newbalanceOrig', 0.0)))
oldbalanceDest = st.number_input('🏦 Old Balance Destination', min_value=0.0, value=float(0.0 if 'reset' in st.session_state else st.session_state.get('oldbalanceDest', 0.0)))
newbalanceDest = st.number_input('🏦 New Balance Destination', min_value=0.0, value=float(0.0 if 'reset' in st.session_state else st.session_state.get('newbalanceDest', 0.0)))

# Store values in session state for persistence
st.session_state.step = step
st.session_state.transaction_type_index = list(le.classes_).index(transaction_type)
st.session_state.amount = amount
st.session_state.oldbalanceOrg = oldbalanceOrg
st.session_state.newbalanceOrig = newbalanceOrig
st.session_state.oldbalanceDest = oldbalanceDest
st.session_state.newbalanceDest = newbalanceDest

# Encode transaction type
transaction_type_encoded = le.transform([transaction_type])[0]

# Buttons aligned properly in the same row with increased spacing
st.markdown('<div class="button-row">', unsafe_allow_html=True)
col1, col2 = st.columns([6, 1])
with col1:
    if st.button('🚦 Predict', key='predict_button'):
        data = pd.DataFrame({
            'step': [step],
            'type': [transaction_type_encoded],
            'amount': [amount],
            'oldbalanceOrg': [oldbalanceOrg],
            'newbalanceOrig': [newbalanceOrig],
            'oldbalanceDest': [oldbalanceDest],
            'newbalanceDest': [newbalanceDest]
        })
        prediction = model.predict(data)
        st.session_state.result = '🚨 Fraudulent Transaction' if prediction[0] == 1 else '✅ Legitimate Transaction'

with col2:
    if st.button('🔄 Reset', key='reset_button'):
        st.session_state.result = None
        for key in ['step', 'transaction_type_index', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']:
            st.session_state[key] = 0 if 'amount' not in key else 0.0
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# Show prediction result
if st.session_state.result is not None:
    st.markdown(f'<h3 class="center-text">Prediction: {st.session_state.result}</h3>', unsafe_allow_html=True)

# Add author name
st.markdown('<p class="center-text" style="margin-top: 150px;">Created by: THOTA KARTHIK NAGA RAJU</p>', unsafe_allow_html=True)

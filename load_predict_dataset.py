import pandas as pd
import numpy as np
import joblib

# Load the saved model and scaler
regressor = joblib.load('stc_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load the dataset
data = pd.read_csv('perm_vol.csv')

# Assuming the dataset has columns 'Time' and 'Pressure' for inputs and 'Permeate_Volume' for actual values
X = data[['Time (min)', 'Pressure (kgf/cm2)']].values  # Input features
y_actual = data['Permeate volume (mL)'].values  # Actual values

# Scale the input data
X_scaled = scaler.transform(X)

# Predict permeate volume for the entire dataset
y_pred = regressor.predict(X_scaled)

# Create a new DataFrame with inputs, actual, and predicted values
results_df = data.copy()  # Copy original data
results_df['Predicted_Permeate_Volume'] = y_pred  # Add predicted values

# Save the results to a new CSV file
results_df.to_csv('perm_vol_predictions.csv', index=False)

print("Predictions completed and saved to 'perm_vol_predictions.csv'.")
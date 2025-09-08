import joblib
import numpy as np

# Load the saved model and scaler
regressor = joblib.load('stc_model.pkl')
scaler = joblib.load('scaler.pkl')


# Function to predict for given T and P values
def predict_permeate_volume(T, P):
    # Ensure inputs are in the correct shape (1, 2) for scaling
    input_data = np.array([[T, P]])

    # Scale the input data
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = regressor.predict(input_scaled)

    return prediction[0]


# Example usage
T_input = float(input("Enter Time (min): "))
P_input = float(input("Enter Pressure (kgf/cm2): "))

predicted_volume = predict_permeate_volume(T_input, P_input)
print(f"Predicted Permeate Volume: {predicted_volume:.4f} mL")
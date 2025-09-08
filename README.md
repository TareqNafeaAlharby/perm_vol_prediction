# Permeate Volume Prediction Model

This project contains a script to load a **optimized model** (selected among multiple models and tuned) and predict permeate volume based on input Time (T) and Pressure (P) values.

## Installation

To install the required dependencies, use the following `pip` command:

```bash
pip install -r requirements.txt
```

Ensure you have a `requirements.txt` file in the same directory with the following content:

```
joblib==1.4.2
numpy==1.26.4
```

## Usage

1. Ensure the trained model (`stc_model.pkl`) and scaler (`scaler.pkl`) files are in the same directory as the script.
2. Run the `load_predict.py` script:
   ```bash
   python load_predict.py
   ```
3. Enter the Time (min) and Pressure (kgf/cm²) values when prompted to get the predicted permeate volume.
4. For Predict on entrie data use:
   ```bash
   python load_predict_dataset.py
   ```

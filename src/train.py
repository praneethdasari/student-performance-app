import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load dataset
data_path = os.path.join(BASE_DIR, "..", "data", "student_data.csv")
data = pd.read_csv(data_path)

# Features & target
X = data[['hours_studied', 'attendance', 'previous_score']]
y = data['final_score']

# Train model
model = LinearRegression()
model.fit(X, y)

# Ensure model folder exists
model_dir = os.path.join(BASE_DIR, "..", "model")
os.makedirs(model_dir, exist_ok=True)

# Save model
model_path = os.path.join(model_dir, "model.pkl")
joblib.dump(model, model_path)

print("✅ Model trained and saved!")
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "..", "model", "model.pkl")
model = joblib.load(model_path)

def predict_score(hours, attendance, previous):
    data = [[hours, attendance, previous]]
    result = model.predict(data)
    return round(result[0], 2)
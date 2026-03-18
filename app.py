from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Absolute path setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model", "model.pkl")

# Load model safely
if not os.path.exists(model_path):
    raise FileNotFoundError("Model file not found. Run train.py first.")

model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        hours = request.form.get('hours', '')
        attendance = request.form.get('attendance', '')
        previous = request.form.get('previous', '')

        # Convert safely
        data = [[float(hours), float(attendance), float(previous)]]
        result = model.predict(data)[0]

        return render_template(
            'index.html',
            prediction=round(result, 2),
            hours=hours,
            attendance=attendance,
            previous=previous
        )

    except ValueError:
        return render_template(
            'index.html',
            prediction="Please enter valid numbers!"
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
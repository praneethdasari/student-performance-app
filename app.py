from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Get absolute path of current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build model path safely
model_path = os.path.join(BASE_DIR, "model", "model.pkl")

# Load model
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        hours = float(request.form['hours'])
        attendance = float(request.form['attendance'])
        previous = float(request.form['previous'])

        data = [[hours, attendance, previous]]
        result = model.predict(data)[0]

        return render_template('index.html', prediction=round(result, 2))

    except:
        return render_template('index.html', prediction="Invalid input!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
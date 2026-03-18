# Student Performance Prediction App

A Machine Learning web application that predicts a student's final score based on study hours, attendance, and previous performance.

---

## Features

* Predict student performance using Linear Regression
* Simple web interface using Flask
* Uses CSV file (no database required)
* Fast and lightweight

---

## Technologies Used

* Python
* pandas
* scikit-learn
* Flask
* joblib

---

## Project Structure

```
Student Performance app/
│
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── data/
│   └── student_data.csv
│
├── model/
│   └── model.pkl
│
├── src/
│   ├── train.py
│   └── predict.py
│
├── requirements.txt
└── README.md
```

---

## How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Train the model

```
python src/train.py
```

### 3. Run the application

```
cd app
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:10000
```

---

## Input Features

* Hours Studied
* Attendance (%)
* Previous Score

---

## Output

* Predicted Final Score

---

## Future Improvements

* Add more features (sleep hours, assignments, etc.)
* Improve UI design
* Add accuracy metrics
* Deploy with custom domain

---

## Author

Praneeth

---

## Description

This project demonstrates a simple Machine Learning workflow using Linear Regression and Flask without using any database.

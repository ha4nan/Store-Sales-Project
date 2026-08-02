# 🏪 Store Sales Prediction System

## 📌 Project Overview

Accurate sales forecasting is essential for retail businesses to effectively manage inventory and meet customer demand. Poor predictions can result in overstock, product waste, or stock shortages, negatively impacting revenue and customer satisfaction.

This project develops a **Machine Learning** model to predict future grocery store sales based on historical sales data. The system includes an interactive **Streamlit** web application that allows users to upload a `test.csv` file, generate sales predictions using a trained **Random Forest Regressor** and **Time- Series-data** , and download the results as a `submission.csv` file.

---

## 🎯 Project Objectives

- Predict future grocery store sales.
- Improve inventory management.
- Reduce overstock and stock shortages.
- Support better business decision-making.

---

## ✨ Features

- Upload a `test.csv` file through a simple web interface.
- Automatic data preprocessing.
- Sales prediction using a trained Random Forest Regression model.
- Download prediction results as `submission.csv`.
- User-friendly Streamlit interface.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 🤖 Machine Learning Model

- **Model:** Random Forest Regressor
- **Task:** Time-Series Sales Forecasting (Regression)
- **Target Variable:** Sales

---

## 📥 Input

- `test.csv`

## 📤 Output

- `submission.csv`

---

## 📂 Project Structure

```text
StoreSalesProject/
│
├── app.py
├── best_model.pkl
├── feature_columns.pkl
├── requirements.txt
├── stores.csv
├── oil.csv
├── run.mp4
└── README.md
```

---

## 🚀 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🔄 Workflow

1. Upload the `test.csv` file.
2. The application automatically preprocesses the uploaded data.
3. The trained Random Forest model generates sales predictions.
4. Download the generated `submission.csv` file.

---

## 🎥 Demo

A screen recording demonstrating how to run and use the application is included in this repository as **run.mp4**.

---

## 👨‍💻 Development Team

- Hager Amr 

- Mohamed Ashraf https://github.com/mody-55

- Hanan Mohamed  https://github.com/ha4nan

- Abdelrahman Nady  bdelrhmnhrb336@gmail.com

- Mohamed Amr https://github.com/mohamedamr222006-alt
---


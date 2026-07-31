🏪 Store Sales Prediction System
📌 Project Overview

Accurate sales forecasting is essential for retail businesses to effectively manage inventory and meet customer demand. Poor predictions can result in overstock, product waste, or stock shortages that negatively impact revenue and customer satisfaction.

This project develops a Machine Learning model to predict future grocery store sales based on historical sales data. The system includes a Streamlit web application that allows users to upload a test.csv file, generate sales predictions using a trained Random Forest Regressor model, and download the results as a submission.csv file.

🎯 Project Objectives
Predict future grocery store sales.
Improve inventory management.
Reduce overstock and stock shortages.
Support better business decision-making.
🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Streamlit
Joblib
🤖 Machine Learning Model
Model: Random Forest Regressor
Target Variable: Sales
📥 Input
test.csv
📤 Output
submission.csv
📂 Project Structure
StoreSalesProject/
│
├── app.py
├── best_model.pkl
├── feature_columns.pkl
├── requirements.txt
├── stores.csv
├── oil.csv
└── README.md
🚀 Installation
pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py
🔄 Workflow
Upload test.csv.
The application preprocesses the data.
The trained model generates sales predictions.
Download the generated submission.csv.
👨‍💻 Development Team
Hager
Mohamed Ashraf
Hanan
Abdelrahman
Mohamed Amr

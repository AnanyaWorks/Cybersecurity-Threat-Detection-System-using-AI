🛡️ AI-Powered Cybersecurity Threat Detection:
This project is a machine learning-based cybersecurity threat detection system built with Python and Flask. It trains an AI model on network traffic data to identify potential security threats and deploys the model via a REST API.

🚀 Features:
Preprocessing and training using the CICIDS2017 dataset,
Random Forest classifier for threat prediction,
Flask-based REST API for real-time predictions,
Postman or Python-based testing,
Easily extendable to use other ML models like XGBoost


🛠️ Tech Stack:
Python 3,
Pandas, NumPy,
scikit-learn,
Flask,
Requests,
Joblib


📂 Project Structure:
Cybersecurity/
├── app.py           # Flask API for threat prediction
├── test.py          # API testing using requests
├── CICIDS2017.csv   # Dataset (not uploaded to GitHub)
├── model.pkl        # Trained model (auto-generated)
├── README.md        # Project info
└── requirements.txt # Python dependencies (optional)


📈 How the Model Works:
Data Cleaning: Removes timestamps, fills missing values.
Feature Engineering: Label encoding + normalization.
Model Training: Random Forest Classifier on CICIDS2017.
API Deployment: Accepts JSON input and returns prediction (True = Threat, False = Safe).


🔧 Setup Instructions:
1. Clone the Repository
2. Install Dependencies:
pip install pandas numpy scikit-learn flask joblib
3. Run the Flask API:
python app.py
4. Test Using Postman or Python:
Send a POST request to http://127.0.0.1:5000/predict with JSON
Expected response:
{
  "Threat_Detected": false
}


📚 Dataset:
CICIDS 2017 Dataset


👩‍💻 Author:
Ananya
GitHub: github.com/AnanyaWorks


# 🩺 Breast Cancer Prediction Web Application (FastAPI + Random Forest)

This project is a **Breast Cancer Prediction Web Application** using:

- **FastAPI** for backend
- **Python / scikit-learn** for Machine Learning
- **Random Forest Classifier** for tumor prediction

The application allows users to input medical features of a patient and receive a prediction of whether the tumor is **Benign** or **Malignant**.

---

## 📁 Project Structure

project/
│
├── backend/
│ ├── main.py # FastAPI application
│ ├── model.pkl # Trained Random Forest model
│ └── schemas.py # Pydantic models for input
│
├── frontend/ # Optional React frontend
│ ├── src/
│ └── public/
│
└── README.md

yaml
Copy code

---

## 🚀 Features

### Backend (FastAPI)
- REST API endpoint: `/predict`
- Input validation using **Pydantic**
- Returns **Benign / Malignant** prediction
- CORS enabled for frontend integration

### Machine Learning
- Random Forest Classifier trained on **Breast Cancer Wisconsin Dataset**
- Fast and reliable predictions
- Model saved as `model.pkl` for deployment

---

## 💻 Installation

### 1. Setup Backend
bash
cd backend
python -m venv venv
# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux / Mac:
source venv/bin/activate
2. Install dependencies
bash
Copy code
pip install fastapi uvicorn scikit-learn pandas
3. Run FastAPI server
bash
Copy code
uvicorn main:app --reload
The API will run at: http://127.0.0.1:8000

🔗 API Endpoint
POST /predict

Request Body Example:

json
Copy code
{
  "radius_mean": 17.99,
  "texture_mean": 10.38,
  "perimeter_mean": 122.8,
  "area_mean": 1001,
  "smoothness_mean": 0.118
}
Response Example:

json
Copy code
{
  "prediction": "Benign"
}

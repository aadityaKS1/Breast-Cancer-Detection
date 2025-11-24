# 🩺 Breast Cancer Prediction Web Application
**Breast Cancer Prediction Using Machine Learning (Random Forest + FastAPI)**

![Breast Cancer](https://i.postimg.cc/q7cCrvng/Screenshot-2025-11-24-224732.png)

---

## Project Overview

This project is a **Breast Cancer Prediction Web Application** that predicts whether a tumor is **Benign** or **Malignant** based on patient medical features.  

**Tech Stack:**  
- Backend: **FastAPI**  
- Machine Learning: **Python + scikit-learn + Random Forest Classifier**  
- Frontend (optional): **React**

---

## Features

- **Backend (FastAPI)**  
  - REST API endpoint: `/predict`  
  - Input validation using **Pydantic**  
  - Returns **Benign / Malignant** prediction  
  - CORS enabled for frontend integration  

- **Machine Learning**  
  - Random Forest Classifier trained on **Breast Cancer Wisconsin Dataset**  
  - High accuracy (~96–97%)  
  - Model saved as `model.pkl` for deployment  

- **Frontend (Optional)**  
  - React form to input patient features  
  - Display prediction results clearly  
  - Input summary & statistics  

---

## Project Folder Structure

```
breast_cancer_app/
│
├─ backend/
│   ├─ main.py                     # FastAPI app
│   ├─ requirements.txt            # Backend dependencies
│   ├─ random_forest_model.pkl     # Trained RF model
│   └─ README.md                   # Backend instructions
│
├─ frontend/                       # React app
│   ├─ public/
│   ├─ src/
│   ├─ package.json
│   └─ README.md
│
├─ notebooks/                      # Optional, for exploration & training
│   └─ main.ipynb
│
└─ README.md                       # Project overview

```

## 💻 Installation

### 1️⃣ Clone Repo
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
 ```
```
2️⃣ Backend Setup
cd backend
python -m venv venv
# Activate venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
pip install fastapi uvicorn scikit-learn pandas numpy pydantic python-multipart
uvicorn main:app --reload


API: http://127.0.0.1:8000

Docs: http://127.0.0.1:8000/docs

3️⃣ Frontend Setup (Optional)
cd frontend
npm install
npm start


Runs at http://localhost:3000
```

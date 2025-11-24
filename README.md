# 🩺 Breast Cancer Prediction Web Application
**Breast Cancer Prediction Using Machine Learning (Random Forest + FastAPI)**

![Breast Cancer](https://cdn-images-1.medium.com/max/2600/1*gNcFEL1cpGpDC4vo1zUAWA.png)

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

```project/
│
├── backend/ # Backend folder (FastAPI + ML model)
│ ├── main.py # FastAPI application
│ ├── model.pkl # Saved Random Forest model
│ └── schemas.py # Pydantic models for input validation
│
├── frontend/ # Optional frontend (React / HTML)
│ ├── src/ # React source code
│ │ └── App.js
│ └── public/ # Public assets (index.html, images)
│
├── images/ # Screenshots for README
│ ├── input_form.png
│ └── result.png
│
└── README.md # Project documentation
```

# Breast Cancer Detection System

Early detection saves lives. This system predicts whether a tumor is
benign or malignant using machine learning — built as a full-stack
application so it is accessible to anyone, not just data scientists.

---

## The Problem

Breast cancer is one of the most common cancers worldwide. Early and
accurate detection significantly improves survival rates. Manual
diagnosis is time-consuming and subject to human error. This system
assists healthcare professionals by providing a fast, data-driven
second opinion.

---

## How It Works

Random Forest classifier trained on the Wisconsin Breast Cancer Dataset.
Features include radius, texture, perimeter, area, and smoothness of
cell nuclei. The model predicts benign or malignant with real-time
results through a web interface.
```
Patient Data Input
↓
Feature Preprocessing + Scaling
↓
Random Forest Classifier
↓
Benign / Malignant Prediction + Confidence Score
```
---

## Results

| Metric | Score |
|---|---|
| Accuracy | 95%+ |
| Evaluation | Accuracy, Precision, ROC-AUC |
| Dataset | Wisconsin Breast Cancer Dataset (WBC) |
| Features | Radius, Texture, Perimeter, Area, Smoothness |

---

## Project Structure
Breast-Cancer-Detection/
│
├── notebook/        # Model training, EDA, feature engineering
├── backend/         # FastAPI backend - model inference and API
├── frontend/        # React frontend - user interface

---

## Tech Stack

**Machine Learning:** Python, Scikit-learn, Pandas, NumPy, Jupyter

**Backend:** FastAPI

**Frontend:** React, HTML, CSS

**Visualization:** Matplotlib, Seaborn

---

## Setup & Run

```bash
# Clone the repo
git clone https://github.com/aadityaKS1/Breast-Cancer-Detection
cd Breast-Cancer-Detection

# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm start
```

Open `http://localhost:3000` in your browser.

---

## Dataset

Wisconsin Breast Cancer Dataset (WBC) - features extracted from
digitized images of fine needle aspirate (FNA) of breast masses.

Features used:
- Radius, Texture, Perimeter, Area
- Smoothness, Compactness, Concavity
- Symmetry, Fractal Dimension

---

## Applications

- Clinical decision support for early breast cancer detection
- Healthcare AI research and education
- Demonstrating full-stack ML deployment in medical contexts

---

## Author

Aaditya Kumar Singh
[LinkedIn](https://www.linkedin.com/in/aadityaks1/) -
[GitHub](https://github.com/aadityaKS1)

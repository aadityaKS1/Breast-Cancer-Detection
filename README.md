# 🩺 Breast Cancer Prediction Web Application (FastAPI + Random Forest)

This project is a **Breast Cancer Prediction Web Application** built using:

- **FastAPI** for backend API development
- **Python / scikit-learn** for Machine Learning
- **Random Forest Classifier** for tumor prediction

The application allows users to input medical features of a patient and receive a prediction of whether the tumor is **Benign** or **Malignant**.

---

## 📁 Project Structure

project/
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
└── README.md # Project documentation


---

## 🚀 Features

### Backend (FastAPI)
- REST API endpoint: `/predict`
- Input validation using **Pydantic**
- Returns **Benign / Malignant** prediction
- CORS enabled for frontend integration
- Easy to extend with additional medical features

### Machine Learning
- Random Forest Classifier trained on **Breast Cancer Wisconsin Dataset**
- High accuracy (~95–97%)
- Model saved as `model.pkl` for deployment

### Frontend (Optional)
- React-based form to input patient features
- Display prediction result clearly
- Optionally show input summary and statistics

---

## 💻 Installation

### 1. Setup Backend
``bash
cd backend
python -m venv venv
# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux / Mac:
source venv/bin/activate
### 2\. Install dependencies

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install fastapi uvicorn scikit-learn pandas   `

### 3\. Run FastAPI server

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   uvicorn main:app --reload   `

*   API runs at: http://127.0.0.1:8000
    
*   Interactive API docs: http://127.0.0.1:8000/docs

from fastapi import  FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd 
from fastapi.middleware.cors import CORSMiddleware

#define severs
origins=[
    "http://localhost:3000",  # React dev server
]
#initialize the fastAPI
app=FastAPI()

# Enable CORS so frontend can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#import the  model
with open ("random_forest_model.pkl","rb") as f:
    model=pickle.load(f)

#define inputs
class PatientData(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    symmetry_mean: float


#create a prediction endpoint
@app.post("/predict")
def predict(data:PatientData):
    #convert input to numpy array
    input_data=pd.DataFrame([{
        'radius_mean': data.radius_mean,
        'texture_mean': data.texture_mean,
        'perimeter_mean': data.perimeter_mean,
        'area_mean': data.area_mean,
        'smoothness_mean': data.smoothness_mean,
        'compactness_mean': data.compactness_mean,
        'concavity_mean': data.concavity_mean,
        'concave points_mean': data.concave_points_mean,
        'symmetry_mean': data.symmetry_mean
    }])
    #make prediction
    prediction=model.predict(input_data)[0]
    
    #return  result
    return {"prediction": int(prediction)}

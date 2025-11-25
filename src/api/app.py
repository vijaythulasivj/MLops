from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI()

MODEL_PATH = "models/model.pkl"

# Load model at startup
if not os.path.exists(MODEL_PATH):
    raise ValueError("Model file not found: models/model.pkl")

model = joblib.load(MODEL_PATH)

# Define input schema
class HousingInput(BaseModel):
    # Modify fields according to your dataset columns
    feature1: float
    feature2: float
    feature3: float
    feature4: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(input_data: HousingInput):
    try:
        df = pd.DataFrame([input_data.dict()])
        prediction = model.predict(df)
        return {"prediction": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

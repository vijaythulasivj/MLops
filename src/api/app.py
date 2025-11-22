from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

MODEL_PATH = "models/model.pkl"
model = pickle.load(open(MODEL_PATH, "rb"))

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": prediction[0]}

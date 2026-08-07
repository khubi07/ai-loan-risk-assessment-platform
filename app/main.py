from fastapi import FastAPI
from schema import LoanRequest
from model import model
import pandas as pd

app = FastAPI()



@app.get("/health")
def health():
    return {"status": "running"}

@app.post("/predict")
def predict(data: LoanRequest):

    input_data = pd.DataFrame([data.dict()])

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    return {
    "prediction": "Approved" if prediction == 1 else "Rejected",
    "approval_probability": round(float(probabilities[1]), 2),
    "rejection_probability": round(float(probabilities[0]), 2)
}
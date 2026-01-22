from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

# Load trained model
model = joblib.load("model.pkl")

app = FastAPI(title="Car Price Prediction API")

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema
class CarInput(BaseModel):
    Present_Price: float
    Kms_Driven: int
    Fuel_Type: str
    Seller_Type: str
    Transmission: str
    Owner: int
    Car_Age: int


@app.get("/health")
def health_check():
    return {"status": "API is running"}


@app.get("/")
def root():
    return {"message": "Welcome to Car Price Prediction API. Use /docs for API documentation."}


@app.post("/predict")
def predict_price(data: CarInput):

    input_data = {
        "Present_Price": data.Present_Price,
        "Kms_Driven": data.Kms_Driven,
        "Fuel_Type": data.Fuel_Type,
        "Seller_Type": data.Seller_Type,
        "Transmission": data.Transmission,
        "Owner": data.Owner,
        "Car_Age": data.Car_Age
    }

    prediction = model.predict(
        np.array([list(input_data.values())])
    )

    return {
        "predicted_price": round(float(prediction[0]), 2)
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

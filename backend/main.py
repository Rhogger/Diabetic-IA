from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.models import request
from src.ia_models import models

app = FastAPI()

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/predict/")
def predict(data: request.RequestBody):
    if data.hypertension:
        data.hypertension = 1
    else:
        data.hypertension = 0

    if data.heart_disease:
        data.heart_disease = 1
    else:
        data.heart_disease = 0

    input_features = [
        [
            data.gender,
            data.age,
            data.hypertension,
            data.heart_disease,
            data.bmi,
            data.hba1c_level,
            data.blood_glucose_level,
        ]
    ]

    y_pred = models.model_diabetes.predict(input_features)[0].astype(int)
    y_prob = models.model_diabetes.predict_proba(input_features)[0].astype(float)

    result = True if y_pred == 1 else False
    probability = y_prob[y_pred]

    return {"diabetic": result, "probability": probability}

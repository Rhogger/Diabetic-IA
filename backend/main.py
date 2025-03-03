from fastapi import FastAPI
from src.models import request
from src.ia_models import models

app = FastAPI()


@app.post("/predict/")
def predict(data: request.RequestBody):
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

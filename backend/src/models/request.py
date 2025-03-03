from pydantic import BaseModel


class RequestBody(BaseModel):
    gender: int
    age: int
    hypertension: bool
    heart_disease: bool
    bmi: float
    hba1c_level: float
    blood_glucose_level: int

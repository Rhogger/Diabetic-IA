import joblib
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(current_dir, "model_diabetes.pkl")
model_diabetes = joblib.load(model_path)

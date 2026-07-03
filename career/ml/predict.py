import joblib
import os
import numpy as np

BASE_DIR = os.path.dirname(__file__)

model = joblib.load(
    os.path.join(BASE_DIR, "career_model.pkl")
)

encoder = joblib.load(
    os.path.join(BASE_DIR, "label_encoder.pkl")
)

scaler = joblib.load(
    os.path.join(BASE_DIR, "scaler.pkl")
)

def predict(features):

    features = np.array(features).reshape(1, -1)

    features = scaler.transform(features)

    prediction = model.predict(features)

    category = encoder.inverse_transform(prediction)

    probability = model.predict_proba(features)

    return category[0], probability[0]
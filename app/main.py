from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import numpy as np
from sklearn.ensemble import IsolationForest
import logging

app = FastAPI(title="Mini Anomaly Detector", version="1.0.1")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("anomaly-detector")

class DataPoint(BaseModel):
    # expects a 3-element vector; change min_items/max_items if you want a different size
    values: conlist(float, min_items=3, max_items=3)

# Initialize a lightweight model for demo purposes
clf = IsolationForest(n_estimators=50, contamination=0.05, random_state=42)
clf.fit(np.random.normal(size=(100, 3)))
logger.info("IsolationForest model trained successfully.")

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}

@app.post("/predict", tags=["Prediction"])
def predict(data: DataPoint):
    try:
        arr = np.array(data.values).reshape(1, -1)
        score = float(-clf.decision_function(arr)[0])
        return {"anomaly_score": score}
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
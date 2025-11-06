# placeholder for future model loading/saving; currently model is created in main.py
# keep file to show separation of concerns for production

from sklearn.ensemble import IsolationForest
import numpy as np


def get_trained_model():
    clf = IsolationForest(n_estimators=50, contamination=0.05, random_state=42)
    clf.fit(np.random.normal(size=(100, 3)))
    return clf
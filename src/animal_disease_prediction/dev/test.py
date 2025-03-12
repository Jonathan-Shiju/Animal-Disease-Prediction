import joblib
from sklearn.preprocessing import StandardScaler
import os
from animal_disease_prediction.utils import config
if __name__ == "__main__":
    scaler = joblib.dump(StandardScaler(), os.path.join("./models", "scaler.joblib"))
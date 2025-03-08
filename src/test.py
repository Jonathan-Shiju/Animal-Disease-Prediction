import joblib
from sklearn.preprocessing import StandardScaler
import os
from utils import config
if __name__ == "__main__":
    scaler = joblib.dump(StandardScaler(), os.path.join("./models", "scaler.joblib"))
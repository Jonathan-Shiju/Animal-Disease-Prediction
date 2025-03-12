import pandas as pd

from animal_disease_prediction.data.load_data import load_data
from animal_disease_prediction.data.preprocessing_input import preprocess_input
from animal_disease_prediction.utils.load_objects import ModelLoader
from animal_disease_prediction.models.predict import predicts
from animal_disease_prediction.utils import config

def predict(data):
    data = pd.DataFrame(data)
    data = preprocess_input(data)
    model = ModelLoader().model
    predictions = model.predict(data)
    return predicts(predictions)

if __name__ == "__main__":
    predict()


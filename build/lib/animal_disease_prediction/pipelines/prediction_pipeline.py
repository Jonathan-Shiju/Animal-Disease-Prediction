
from data.load_data import load_data

from data.preprocessing_input import preprocess_input
from animal_disease_prediction.utils.load_objects import ModelLoader
from models.predict import predicts
from animal_disease_prediction.utils import config

def predict():
    data = load_data()
    print(data.loc[260, config.target_col])
    data = preprocess_input(data.iloc[[260], :].drop(columns=config.target_col).copy())
    model = ModelLoader().model
    predictions = model.predict(data)
    return predicts(predictions)

if __name__ == "__main__":
    predict()


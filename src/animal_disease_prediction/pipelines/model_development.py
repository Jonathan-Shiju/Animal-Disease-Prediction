from animal_disease_prediction.data.load_data import load_data
from animal_disease_prediction.data.preprocessing import preprocess

from animal_disease_prediction.models.train_model import train_model
from animal_disease_prediction.models.evaluate_model import evaluate_model

from animal_disease_prediction.utils import config

def model_development():
    data = load_data()
    X_train, X_test, y_train, y_test, class_dicts, weight_dict = preprocess(data)
    config.model_dict = train_model(X_train, y_train)
    evaluate_model(config.model_dict, X_test, y_test, X_train, y_train)
import json
from animal_disease_prediction.utils import config
def predicts(pred_encoded):
    with open(config.class_dicts_path, 'r') as f:
        class_dict = json.load(f)
    predictions = class_dict[str(pred_encoded[0])]
    return predictions
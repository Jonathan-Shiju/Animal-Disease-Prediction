import joblib
from utils import config
import json

class ModelLoader:
    def __init__(self):
        self.scaler = None
        self.encoder = None
        self.constant_filter = None
        self.selector = None
        self.class_dicts = None
        self.model = None
        self.one_hot_encoder = None
        self.load_objects()

    def load_objects(self):
        # Load the label encoder
        self.encoder = joblib.load(config.encoders_path)
        # Load the StandardScaler
        self.scaler = joblib.load(config.scaler_path)
        # Load the feature selector
        self.selector = joblib.load(config.selector_path)
        # Load the constant feature filter
        self.constant_filter = joblib.load(config.constant_filter_path)
        # Load the class dictionary
        with open(config.class_dicts_path, 'r') as f:
            self.class_dicts = json.load(f)
        # Load the model
        self.model = joblib.load(config.rf_model_path)
        # Load the one-hot encoder
        self.one_hot_encoder = joblib.load(config.one_hot_encoder_path)
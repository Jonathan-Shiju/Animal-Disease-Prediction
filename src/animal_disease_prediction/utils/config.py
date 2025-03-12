import importlib.resources as pkg_resources
import animal_disease_prediction

target_col = 'Disease_Prediction'

symptom_cols = ['Appetite_Loss', 'Vomiting', 'Diarrhea', 'Coughing','Labored_Breathing', 'Lameness', 'Skin_Lesions','Nasal_Discharge', 'Eye_Discharge']

num_features = ['Age', 'Weight', 'Body_Temperature', 'Duration_Num']

cat_features = ['Animal_Type', 'Breed', 'Gender', 'Age_Group', 'Weight_Category']


def get_resource_path(file_name):
    return str(pkg_resources.files(animal_disease_prediction) / "models" / file_name)

# Paths (Updated)
encoders_path = get_resource_path("encoders.joblib")
scaler_path = get_resource_path("scaler.joblib")
selector_path = get_resource_path("selector.joblib")
constant_filter_path = get_resource_path("constant_filter.joblib")
class_dicts_path = get_resource_path("class_dicts.json")
rf_model_path = get_resource_path("rf_model.joblib")
xgb_model_path = get_resource_path("xgb_model.joblib")
one_hot_encoder_path = get_resource_path("one_hot_encoder.joblib")

def get_dataset_path():
    return str(pkg_resources.files(animal_disease_prediction) / "data/cleaned_animal_disease_prediction.csv")

Dataset = get_dataset_path()
target_col = 'Disease_Prediction'

symptom_cols = ['Appetite_Loss', 'Vomiting', 'Diarrhea', 'Coughing','Labored_Breathing', 'Lameness', 'Skin_Lesions','Nasal_Discharge', 'Eye_Discharge']

num_features = ['Age', 'Weight', 'Body_Temperature', 'Duration_Num']

cat_features = ['Animal_Type', 'Breed', 'Gender', 'Age_Group', 'Weight_Category']

Dataset = '../data/raw/cleaned_animal_disease_prediction.csv'

encoders_path = './models/encoders.joblib'

scaler_path = './models/scaler.joblib'

selector_path = './models/selector.joblib'
constant_filter_path = './models/constant_filter.joblib'

class_dicts_path = './models/class_dicts.json'

rf_model_path = './models/rf_model.joblib'

xgb_model_path = './models/xgb_model.joblib'

model_dict = None

one_hot_encoder_path = './models/one_hot_encoder.joblib'


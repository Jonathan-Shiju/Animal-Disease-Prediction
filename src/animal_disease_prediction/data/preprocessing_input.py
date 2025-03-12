from animal_disease_prediction.utils import config
import numpy as np
import pandas as pd
from animal_disease_prediction.utils.load_objects import ModelLoader

def categorize_weight(row):
    if row['Animal_Type'] == 'Dog':
        bins = [0, 10, 25, 40, float('inf')]
        labels = ['Small', 'Medium', 'Large', 'Giant']
    elif row['Animal_Type'] == 'Cat':
        bins = [0, 4, 6, 8, float('inf')]
        labels = ['Small', 'Medium', 'Large', 'Giant']
    else:
        return 'NA'
    return pd.cut([row['Weight']], bins=bins, labels=labels)[0]

def categorize_age(row):
    if row['Animal_Type'] == 'Dog':
        bins = [0, 1, 3, 5, 10, float('inf')]
        labels = ['Infant', 'Young', 'Adult', 'Middle_Aged', 'Senior']
    elif row['Animal_Type'] == 'Cat':
        bins = [0, 1, 3, 5, 10, float('inf')]
        labels = ['Infant', 'Young', 'Adult', 'Middle_Aged', 'Senior']
    else:
        return 'NA'
    return pd.cut([row['Age']], bins=bins, labels=labels)[0]


def preprocess_input(data):
    model_loader = ModelLoader()

    scaler = model_loader.scaler
    encoders = model_loader.encoder
    selector = model_loader.selector
    constant_filter = model_loader.constant_filter
    class_dicts = model_loader.class_dicts
    one_hot_encoder = model_loader.one_hot_encoder

    # Binary encoding of symptoms
    for col in config.symptom_cols:
        data[col] = data[col].apply(lambda x: 1 if x == 'Yes' else 0)

    # Replace temperature column
    data['Body_Temperature'] = data['Body_Temperature'].astype(str).str.replace('°C', '', regex=False).astype(float)

    # Duration to numerical
    data['Duration_Num'] = data['Duration'].str.extract('(\d+)').astype(float)
    data.loc[data['Duration'].str.contains('week'), 'Duration_Num'] *= 7
    
    # Age categorization
    data['Age_Group'] = data.apply(categorize_age, axis=1)

    # Weight categorization
    data['Weight_Category'] = data.apply(categorize_weight, axis=1)

    # One-hot encoding of categorical columns
    for col, encoder in encoders.items():
        data[col] = data[col].astype(str)
        data[col] = data[col].apply(lambda x: encoder.transform([x])[0] if x in encoder.classes_ else -1)
    
    # Scaling numerical columns
    data[config.num_features] = scaler.transform(data[config.num_features])
    
    # One-hot encoding of object columns
    objs_data = data.select_dtypes(['object']).columns
    data = one_hot_encoder.transform(data[objs_data])
    data = pd.DataFrame(data, columns=one_hot_encoder.get_feature_names_out())

    # Remove features with low variance
    data = data.loc[:, constant_filter.get_support()]
    print(data)
    # Feature selection
    data = selector.transform(data)
    return data

import pandas as pd
import numpy as np
import seaborn as sns
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif
import json

from animal_disease_prediction.utils import config

from data.feature_scaling import feature_scaling

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

def preprocess(data):
    value_counts = data[config.target_col].value_counts(normalize=True)
    rare_classes = value_counts[value_counts < 0.02].index
    data[config.target_col] = data[config.target_col].apply(lambda x: 'Other' if x in rare_classes else x)

    for col in config.symptom_cols:
        data[col] = data[col].apply(lambda x: 1 if x == 'Yes' else 0)

    data['Body_Temperature'] = data['Body_Temperature'].astype(str).str.replace('°C', '', regex=False).astype(float)

    data['Duration_Num'] = data['Duration'].str.extract('(\d+)').astype(float)
    data.loc[data['Duration'].str.contains('week'), 'Duration_Num'] *= 7

    data['Age_Group'] = pd.cut(data['Age'], bins=[0, 1, 3, 5, 10, float('inf')], labels=['Infant', 'Young', 'Adult', 'Middle_Aged', 'Senior'])

    data['Weight_Category'] = data.apply(categorize_weight, axis=1)

    X = data.drop(columns=[config.target_col])
    y = data[config.target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    X_train, X_test, y_train, y_test, class_dicts, weight_dict = feature_scaling(X_train, X_test, y_train, y_test)

    # Remove features with low variance
    constant_filter = VarianceThreshold(threshold=0.01)
    constant_filter.fit(X_train)

    X_train = X_train.loc[:, constant_filter.get_support()]
    X_test = X_test.loc[:, constant_filter.get_support()]

    selector = SelectKBest(f_classif, k=20)
    X_train_fs = selector.fit_transform(X_train, y_train)
    X_test_fs = selector.transform(X_test)

    joblib.dump(selector, config.selector_path)
    joblib.dump(constant_filter, config.constant_filter_path)

    
    with open(config.class_dicts_path, 'w') as f:
        json.dump(class_dicts, f)
    
    return X_train_fs, X_test_fs, y_train, y_test, class_dicts, weight_dict
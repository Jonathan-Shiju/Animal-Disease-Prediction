from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.utils.class_weight import compute_class_weight
import joblib
import pandas as pd
import numpy as np


from animal_disease_prediction.utils import config

def labelEncoding(X_train, X_test, y_train, y_test):
    encoders = {}
    for col in config.cat_features:
        X_train[col] = X_train[col].astype(str)
        X_test[col] = X_test[col].astype(str)
        all_classes = np.unique(X_train[col].tolist() + X_test[col].tolist())
        encoder = LabelEncoder()
        encoder.fit(all_classes)
        encoders[col] = encoder
        X_train[col] = encoder.transform(X_train[col])
        X_test[col] = X_test[col].apply(
        lambda x: encoder.transform([x])[0] if x in encoder.classes_ else -1)

    # One-hot encode
    objs_train = X_train.select_dtypes(['object']).columns
    one_hot_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    one_hot_encoder.fit(X_train[objs_train])
    X_train = one_hot_encoder.transform(X_train[objs_train])
    X_test = one_hot_encoder.transform(X_test[objs_train])

    X_train = pd.DataFrame(X_train, columns=one_hot_encoder.get_feature_names_out())
    X_test = pd.DataFrame(X_test, columns=one_hot_encoder.get_feature_names_out())

    print(X_train)
    print(X_train.shape)

    joblib.dump(one_hot_encoder, config.one_hot_encoder_path)

    # Encode y_train and y_test
    y_le = LabelEncoder()
    y_train_encoded = y_le.fit_transform(y_train)
    y_test_encoded = y_le.transform(y_test)
    # Compute class weights
    class_weights = compute_class_weight(
        class_weight='balanced',
        classes=np.unique(y_train_encoded),
        y=y_train_encoded
    )

    # Store class weights
    weights_dict = dict(zip(np.unique(y_train_encoded), class_weights))

    y_test_not_encoded = y_le.inverse_transform(y_test_encoded)
    class_dict = dict(zip(np.unique(y_test_encoded).astype(str), np.unique(y_test_not_encoded)))

    joblib.dump(encoders, config.encoders_path)
    return X_train, X_test, y_train_encoded, y_test_encoded, class_dict, weights_dict

def feature_scaling(X_train, X_test, y_train, y_test):
    scaler = StandardScaler()
    X_train[config.num_features] = scaler.fit_transform(X_train[config.num_features])
    X_test[config.num_features] = scaler.transform(X_test[config.num_features])
    joblib.dump(scaler, config.scaler_path)
    return labelEncoding(X_train, X_test, y_train, y_test)
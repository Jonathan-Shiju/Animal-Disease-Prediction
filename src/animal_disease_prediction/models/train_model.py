import joblib
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, make_scorer
from xgboost import XGBClassifier
import sklearn
from models.evaluate_model import evaluate_model

from animal_disease_prediction.utils import config

def train_model(X_train, y_train):
    # Define Scoring
    f1_macro_scorer = make_scorer(f1_score, average='macro')

    rf_base = RandomForestClassifier(random_state=42)

    xgb_base = XGBClassifier(
        eval_metric='mlogloss',
        random_state=42)

    rf_param_dist = {
    'n_estimators': [40, 50, 60],
    'max_depth': [5, 10, None],
    'min_samples_split': [2, 5, 10],
    'class_weight': ['balanced']
    }
    xgb_param_dist = {
        'learning_rate': [0.01, 0.1, 0.2],
        'max_depth': [3, 6, 10],
        'n_estimators': [50, 100, 200],
        'subsample': [0.8, 1.0],
        'colsample_bytree': [0.8, 1.0]
    }

    # Random Search for RF and XGB
    rf_random_search = RandomizedSearchCV(
        estimator=rf_base,
        param_distributions=rf_param_dist,
        n_iter=8,
        scoring=f1_macro_scorer,
        cv=3,
        n_jobs=-1,
        random_state=42
    )

    xgb_random_search = RandomizedSearchCV(
        estimator=xgb_base,
        param_distributions=xgb_param_dist,
        n_iter=8,
        scoring=f1_macro_scorer,
        cv=3,
        n_jobs=-1,
        random_state=42
    )

    rf_random_search.fit(X_train, y_train)
    xgb_random_search.fit(X_train, y_train)

    rf_best = rf_random_search.best_estimator_
    xgb_best = xgb_random_search.best_estimator_  

    joblib.dump(rf_best, config.rf_model_path)
    joblib.dump(xgb_best, config.xgb_model_path) 

    model_dicts = {
        'Names': ['Random Forest', 'XGBoost'],
        'Models': [rf_best, xgb_best]
    }
    
    return model_dicts
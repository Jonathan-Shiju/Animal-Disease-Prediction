.
├── MANIFEST.in
├── README.md
├── data
│   └── raw
│       └── cleaned_animal_disease_prediction.csv
├── notebooks
│   ├── Evaluation.ipynb
│   ├── ModelTraining.ipynb
│   ├── PreProcessing.ipynb
│   └── Visualization.ipynb
├── pyproject.toml
└── src
    ├── __init__.py
    ├── data
    │   ├── __init__.py
    │   ├── feature_scaling.py
    │   ├── load_data.py
    │   ├── preprocessing.py
    │   └── preprocessing_input.py
    ├── main.py
    ├── models
    │   ├── __init__.py
    │   ├── class_dicts.json
    │   ├── constant_filter.joblib
    │   ├── encoders.joblib
    │   ├── evaluate_model.py
    │   ├── one_hot_encoder.joblib
    │   ├── predict.py
    │   ├── rf_model.joblib
    │   ├── scaler.joblib
    │   ├── selector.joblib
    │   ├── train_model.py
    │   └── xgb_model.joblib
    ├── pipelines
    │   ├── __init__.py
    │   ├── model_development.py
    │   └── prediction_pipeline.py
    ├── test.py
    ├── test_data.py
    ├── test_models.py
    ├── test_utils.py
    └── utils
        ├── __init__.py
        ├── config.py
        ├── load_objects.py
        └── logging.py

9 directories, 38 files

.
├── MANIFEST.in
├── README.md
├── backend
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── model_loader.py
│   └── routes.py
├── data
│   └── cleaned_animal_disease_prediction.csv
├── dist
│   ├── animal_disease_prediction-0.1.0-py3-none-any.whl
│   └── animal_disease_prediction-0.1.0.tar.gz
├── notebooks
│   ├── Evaluation.ipynb
│   ├── ModelTraining.ipynb
│   ├── PreProcessing.ipynb
│   └── Visualization.ipynb
├── pyproject.toml
├── requirements.txt
└── src
    ├── animal_disease_prediction
    │   ├── __init__.py
    │   ├── data
    │   │   ├── __init__.py
    │   │   ├── feature_scaling.py
    │   │   ├── load_data.py
    │   │   ├── preprocessing.py
    │   │   └── preprocessing_input.py
    │   ├── dev
    │   │   ├── main.py
    │   │   ├── test.py
    │   │   ├── test_data.py
    │   │   ├── test_models.py
    │   │   └── test_utils.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   ├── class_dicts.json
    │   │   ├── constant_filter.joblib
    │   │   ├── encoders.joblib
    │   │   ├── evaluate_model.py
    │   │   ├── one_hot_encoder.joblib
    │   │   ├── predict.py
    │   │   ├── rf_model.joblib
    │   │   ├── scaler.joblib
    │   │   ├── selector.joblib
    │   │   ├── train_model.py
    │   │   └── xgb_model.joblib
    │   ├── pipelines
    │   │   ├── __init__.py
    │   │   ├── model_development.py
    │   │   └── prediction_pipeline.py
    │   ├── prediction.egg-info
    │   │   ├── PKG-INFO
    │   │   ├── SOURCES.txt
    │   │   ├── dependency_links.txt
    │   │   ├── requires.txt
    │   │   └── top_level.txt
    │   └── utils
    │       ├── __init__.py
    │       ├── config.py
    │       └── load_objects.py
    └── animal_disease_prediction.egg-info
        ├── PKG-INFO
        ├── SOURCES.txt
        ├── dependency_links.txt
        ├── requires.txt
        └── top_level.txt

14 directories, 55 files

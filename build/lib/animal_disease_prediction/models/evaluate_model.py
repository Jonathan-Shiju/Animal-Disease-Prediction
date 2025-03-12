from sklearn.metrics import classification_report, accuracy_score
import numpy as np
import matplotlib.pyplot as plt

from animal_disease_prediction.utils import config
import json

def evaluate_model(model_dict, X_test, y_test, X_train, y_train):
    with open(config.class_dicts_path, 'r') as f:
        class_dict = json.load(f)
    for model_name, model in zip(model_dict['Names'], model_dict['Models']):
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        test_classes = np.unique(y_test)
        target_names = [decoded for _, decoded in class_dict.items()]

        report = classification_report(
        y_test,
        y_pred,
        labels=test_classes,
        target_names=target_names,
        zero_division=1
    )
   
        print(f"=== {model_name} ===")
        print(f"Accuracy: {accuracy:.4f}")
        # Generate classification report
        report_dict = classification_report(
            y_test,
            y_pred,
            labels=test_classes,
            target_names=target_names,
            zero_division=1,
            output_dict=True
        )

        # Visualize report
        categories = list(report_dict.keys())[:-3]
        precision = [report_dict[category]['precision'] for category in categories]
        recall = [report_dict[category]['recall'] for category in categories]
        f1_score = [report_dict[category]['f1-score'] for category in categories]

        # Plot categories
        x = np.arange(len(categories))
        bar_width = 0.25

        # Plot the bars
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.bar(x - bar_width, precision, bar_width, label='Precision', color='blue')
        ax.bar(x, recall, bar_width, label='Recall', color='orange')
        ax.bar(x + bar_width, f1_score, bar_width, label='F1-Score', color='green')

        # Label the plot
        ax.set_xlabel('Classes', fontsize=14)
        ax.set_ylabel('Scores', fontsize=14)
        ax.set_title(f'Classification Report Visualization for {model_name}', fontsize=16)
        ax.set_xticks(x)
        ax.set_xticklabels(categories, rotation=45, ha='right', fontsize=12)
        ax.legend(fontsize=12)
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        # Show the plot
        plt.tight_layout()
        plt.show()
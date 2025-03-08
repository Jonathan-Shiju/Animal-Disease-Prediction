import sys
import os

sys.path.append(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")), "src"))

from utils import config
from pipelines.prediction_pipeline import predict
from pipelines.model_development import model_development

if __name__ == "__main__":
    print(f'Predicted Disease: {predict()}')
    #model_development()
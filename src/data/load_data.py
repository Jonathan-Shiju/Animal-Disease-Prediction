import sys
import pandas as pd
import os

from utils import config

def load_data():
    # Load the data
    if not os.path.exists(config.Dataset):
        raise FileNotFoundError(f"File not found at {config.Dataset}")
    data = pd.read_csv(config.Dataset)
    return data
    
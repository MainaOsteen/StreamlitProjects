import pandas as pd
import numpy as np
from tabulate import tabulate


def load_data():
    df = pd.read_csv("tracks_features.csv")
    return df

data = load_data()
print(tabulate(data.head()))




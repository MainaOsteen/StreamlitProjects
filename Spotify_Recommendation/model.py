#%%
import pandas as pd
import numpy as np
import ast


def load_data():
    df = pd.read_csv("tracks_features.csv")
    return df

data = load_data()
print(data.head())


#%%
missing_values = data.isnull().any().sum()


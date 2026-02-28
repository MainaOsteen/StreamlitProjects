from model import data
from tabulate import tabulate

def clean_data(df):

    df.fillna({
        "name":"Unknown",
        "album":"Unknown"
    }, inplace=True)

    cols = ["album", "artists"]
    df[cols] = df[cols].apply(lambda x: x.str.replace(r"[\[\],/'']", "", regex=True).str.strip())

    df["artists"] = df["name"] + "---" + df["artists"]

    df.reset_index(drop = True, inplace=True)

    return df

cd_data = clean_data(data)

from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

feature_cols = ["danceability", "tempo", "liveness", "valence", "instrumentalness", "acousticness", "loudness", "speechiness"]

import faiss
from sklearn.preprocessing import StandardScaler
def initialize_engine(cd_data):

    X = cd_data[feature_cols].values.astype('float32')
    X = np.ascontiguousarray(X)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    faiss.normalize_L2(X_scaled)
 
 
    d = X_scaled.shape[1]  
    index = faiss.IndexFlatIP(d)
    index.add(X_scaled)


    k=10
    distances, indices = index.search(X_scaled[500:501], k)
  

    recommended_indices = indices[0][1:] 
    recommendations = cd_data.iloc[recommended_indices]

    return X_scaled, index








import numpy as np
import pandas as pd

def get_features(row):
     
    feature_vals = []
    
    features = {
    'danceability':0.0,
    'energy':0.0, 
    'key':0.0, 
    'loudness':0.0, 
    'mode':0, 
    'speechiness':0.0,
    'acousticness':0.0,
    'instrumentalness':0.0,
    'liveness':0.0,
    'valence':0.0,
    'tempo':0.0, 
    'type':'', 
    'id':'', 
    'uri':0.0, 
    'track_href':0.0,
    'analysis_url':0.0,
    'duration_ms':0.0,
    'time_signature':0.0,}
    
    for key, val in row['Features'].tolist().items():
        try:
            #print(key, val)
            features[key] = val
            
        except:
            #error message in case something goes wrong
            print("Failed to add:", row['TrackID'], "when inserting feature", key, "with value", val)
            
    for key, val in features.items():
        feature_vals.append(val)
    
    return pd.Series(feature_vals)


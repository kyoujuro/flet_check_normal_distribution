import numpy as np

def detect_outliers(data, threhold):
    mean = np.mean(data)
    std = np.std(data)
    
    outliers = []
    for value in data:
        z_score = (value - mean) / std
        if np.abs(z_score) > threshold:
            outliers.append(value)
    return outliers

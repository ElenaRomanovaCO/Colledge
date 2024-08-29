import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt



def load_time_series(file_path):
    return pd.read_csv(file_path)

def handle_missing_values(data, method='linear'):
    return data.interpolate(method=method)

def normalize_data(data):
    return (data - data.min()) / (data.max() - data.min())

def simple_moving_average(data, window):
    return data.rolling(window=window, center=True).mean()

# def decompose_time_series(data, window=12):
#     trend = simple_moving_average(data, window)
#     seasonal = data - trend
#     return pd.DataFrame({
#         'observed': data,
#         'trend': trend,
#         'seasonal': seasonal,
#         'residual': data - (trend + seasonal)
#     })

def decompose_time_series(series):
    # Ensure the series has a datetime index
    if not isinstance(series.index, pd.DatetimeIndex):
        series = series.reset_index(drop=True)
        series.index = pd.date_range(start='2023-01-01', periods=len(series), freq='D')

    # Perform the decomposition
    result = seasonal_decompose(series, model='additive', extrapolate_trend='freq')
    return result
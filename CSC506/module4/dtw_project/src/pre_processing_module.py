import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler


# def load_and_preprocess_time_series(directory='data/generated_time_series'):
#     """
#     Load and preprocess all time series files in the specified directory.
#
#     :param directory: Directory containing the time series CSV files
#     :return: Dictionary of normalized DataFrames, one for each time series
#     """
#     normalized_dfs = {}
#
#     for filename in os.listdir(directory):
#         if filename.endswith('.csv'):
#             file_path = os.path.join(directory, filename)
#             series_name = os.path.splitext(filename)[0]
#
#             # Load the time series
#             df = pd.read_csv(file_path)
#
#             # Normalize the data
#             normalized_df = normalize_data(df)
#
#             normalized_dfs[series_name] = normalized_df
#
#     return normalized_dfs
#
#
# def normalize_data(df, methods=['min_max', 'z_score', 'decimal', 'robust']):
#     normalized_df = pd.DataFrame()
#     normalized_df['date'] = df['date']
#
#     for column in df.columns:
#         if column != 'date':
#             series = df[column]
#
#             if 'min_max' in methods:
#                 normalized_df[f'{column}_min_max'] = min_max_normalize(series)
#
#             if 'z_score' in methods:
#                 normalized_df[f'{column}_z_score'] = z_score_normalize(series)
#
#             if 'decimal' in methods:
#                 normalized_df[f'{column}_decimal'] = decimal_scaling(series)
#
#             if 'robust' in methods:
#                 normalized_df[f'{column}_robust'] = robust_normalize(series)
#
#     return normalized_df




def min_max_normalize(series):
    scaler = MinMaxScaler()
    normalized = scaler.fit_transform(series.values.reshape(-1, 1))
    return normalized.flatten()

def z_score_normalize(series):
    scaler = StandardScaler()
    normalized = scaler.fit_transform(series.values.reshape(-1, 1))
    return normalized.flatten()

def decimal_scaling(series):
    max_abs_value = series.abs().max()
    scaling_factor = 10 ** np.ceil(np.log10(max_abs_value + 1))
    return series / scaling_factor

def robust_normalize(series):
    scaler = RobustScaler()
    normalized = scaler.fit_transform(series.values.reshape(-1, 1))
    return normalized.flatten()

def load_and_preprocess_time_series(directory='data/generated_time_series'):
    """
    Load and preprocess all time series files in the specified directory.

    :param directory: Directory containing the time series CSV files
    :return: Dictionary of normalized DataFrames, one for each time series
    """
    normalized_dfs = {}

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            series_name = os.path.splitext(filename)[0]

            # Load the time series
            df = pd.read_csv(file_path)

            # Normalize the data
            normalized_df = normalize_data(df)

            normalized_dfs[series_name] = normalized_df
    print(f"{normalized_dfs=}")

    return normalized_dfs


def normalize_data(df, methods=['min_max', 'z_score', 'decimal', 'robust']):
    normalized_df = pd.DataFrame()
    normalized_df['date'] = df['date']

    for column in df.columns:
        if column != 'date':
            series = df[column]

            if 'min_max' in methods:
                normalized_df[f'{column}_min_max'] = min_max_normalize(series)

            if 'z_score' in methods:
                normalized_df[f'{column}_z_score'] = z_score_normalize(series)

            if 'decimal' in methods:
                normalized_df[f'{column}_decimal'] = decimal_scaling(series)

            if 'robust' in methods:
                normalized_df[f'{column}_robust'] = robust_normalize(series)

    return normalized_df
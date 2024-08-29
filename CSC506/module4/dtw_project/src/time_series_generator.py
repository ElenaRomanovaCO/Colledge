import pandas as pd
import numpy as np
import os


def generate_time_series(n_series, date_starts, days, frequency):
    # Set a seed for reproducibility
    np.random.seed(42)

    series_dict = {}

    for i in range(n_series):
        # Generate a date range for each series
        dates = pd.date_range(date_starts[i], periods=days, freq=frequency)

        # Generate random values
        values = np.random.randn(days).cumsum()

        # Create a DataFrame for this series
        df = pd.DataFrame({
            'date': dates,
            'value': values
        })

        series_dict[f'series_{i+1}'] = df

    return series_dict



# def generate_time_series(n_series, length, means, std_devs):
#     """
#     Generate n number of time series.
#
#     :param n_series: Number of time series to generate
#     :param length: Length of each time series
#     :param means: List of means for each series (or single value for all)
#     :param std_devs: List of standard deviations for each series (or single value for all)
#     :return: Dictionary of DataFrames, each containing a single time series
#     """
    # if isinstance(means, (int, float)):
    #     means = [means] * n_series
    # if isinstance(std_devs, (int, float)):
    #     std_devs = [std_devs] * n_series
    #
    # if len(means) != n_series or len(std_devs) != n_series:
    #     raise ValueError("Length of means and std_devs must match n_series")
    #
    # series_dict = {}
    # for i in range(n_series):
    #     series_name = f'series_{i + 1}'
    #     series_data = np.random.normal(means[i], std_devs[i], length)
    #     series_dict[series_name] = pd.DataFrame({series_name: series_data})
    #
    # return series_dict

# def generate_time_series(n_series, date_starts, days, frequency):
#     # Set a seed for reproducibility
#     np.random.seed(42)
#
#     # Generate a date range
#     dates = pd.date_range('2023-01-01', periods=100, freq='D')
#
#     # Generate random values
#     values = np.random.randn(100).cumsum()
#
#     # Create a DataFrame
#     df = pd.DataFrame({'date': dates, 'value': values})
#
#     print(df)

    # def generate_two_time_series(n_days, start_date='2023-01-01', freq='D'):
    #     # Set a seed for reproducibility
    #     np.random.seed(42)
    #
    #     # Generate a date range
    #     dates = pd.date_range(start_date, periods=n_days, freq=freq)
    #
    #     # Generate random values for two series
    #     values1 = np.random.randn(n_days).cumsum()
    #     values2 = np.random.randn(n_days).cumsum()
    #
    #     # Create a DataFrame with both series
    #     df = pd.DataFrame({
    #         'date': dates,
    #         'series1': values1,
    #         'series2': values2
    #     })
    #
    #     return df

    # series_dict = {}
    # for i in range(n_series):
    #     series_name = f'series_{i + 1}'
    #     # dates = pd.date_range('2023-01-01', periods=100, freq='D')
    #     dates = pd.date_range(start=date_starts, periods=days, freq=frequency)
    #     values = np.random.randn(100).cumsum()
    #
    #
    #     series_data = df = pd.DataFrame({'date': dates, 'value': values})
    #     series_dict[series_name] = pd.DataFrame({series_name: series_data})
    #     print(f"{series_data=}, {series_name=}")
    #     print(f"{series_dict=}")
    #
    #     print(f"{series_dict[series_name]=}")
    #
    # return series_dict



# def create_time_series_files(n_series, length, means, std_devs, output_dir='data/generated_time_series'):
#     """
#     Generate time series and save them to separate files.
#
#     :param n_series: Number of time series to generate
#     :param length: Length of each time series
#     :param means: List of means for each series (or single value for all)
#     :param std_devs: List of standard deviations for each series (or single value for all)
#     :param output_dir: Directory to save the time series files
#     :return: List of file paths where time series are saved
#     """
#     os.makedirs(output_dir, exist_ok=True)
#
#     series_dict = generate_time_series(n_series, length, means, std_devs)
#
#     file_paths = []
#     for series_name, series_df in series_dict.items():
#         filename = os.path.join(output_dir, f'{series_name}.csv')
#         series_df.to_csv(filename, index=False)
#         file_paths.append(filename)
#         print(f"Time series {series_name} saved to '{filename}'")
#
#     return file_paths


def create_time_series_files(n_series, date_starts, days, frequency, output_dir='data/generated_time_series'):
    """
    Generate time series and save them to separate files.

    :param n_series: Number of time series to generate (should be 2 for this case)
    :param date_starts: List of start dates for each series
    :param days: Number of days for each series
    :param frequency: Frequency of the time series (e.g., 'D' for daily)
    :param output_dir: Directory to save the time series files
    :return: List of file paths where time series are saved
    """
    os.makedirs(output_dir, exist_ok=True)

    # Ensure we're generating exactly 2 series
    # n_series = 2
    # if len(date_starts) != n_series:
    #     raise ValueError("Please provide exactly 2 start dates for the 2 series.")

    series_dict = generate_time_series(n_series, date_starts, days, frequency)

    file_paths = []
    for series_name, series_df in series_dict.items():
        filename = os.path.join(output_dir, f'{series_name}.csv')
        series_df.to_csv(filename, index=False)
        file_paths.append(filename)
        print(f"Time series {series_name} saved to '{filename}'")

    return file_paths

# def create_time_series_files(n_series, date_starts, days, frequency, output_dir='data/generated_time_series'):
#     """
#     Generate time series and save them to separate files.
#
#     :param n_series: Number of time series to generate
#     :param length: Length of each time series
#     :param means: List of means for each series (or single value for all)
#     :param std_devs: List of standard deviations for each series (or single value for all)
#     :param output_dir: Directory to save the time series files
#     :return: List of file paths where time series are saved
#     """
#     os.makedirs(output_dir, exist_ok=True)
#
#     series_dict = generate_time_series(n_series, date_starts, days, frequency)
#
#     file_paths = []
#     for series_name, series_df in series_dict.items():
#         filename = os.path.join(output_dir, f'{series_name}.csv')
#         series_df.to_csv(filename, index=False)
#         file_paths.append(filename)
#         print(f"Time series {series_name} saved to '{filename}'")
#
#     return file_paths


def print_time_series_summary(series_dict):
    """
    Print summary statistics for each time series.

    :param series_dict: Dictionary of time series DataFrames
    """
    print("\nGenerated Time Series Summary:")
    for series_name, series_df in series_dict.items():
        print(f"\n{series_name}:")
        print(series_df.describe())
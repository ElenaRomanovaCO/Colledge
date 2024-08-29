import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt




def plot_time_series(dfs, output_dir='plots/time_series'):
    """
    Plot all time series in the given dictionary of DataFrames.

    :param dfs: Dictionary of DataFrames, each containing a time series
    :param output_dir: Directory to save the plot images
    """
    os.makedirs(output_dir, exist_ok=True)

    for series_name, df in dfs.items():
        plt.figure(figsize=(12, 6))
        plt.plot(df.index, df.iloc[:, 0])
        plt.title(f'Time Series: {series_name}')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.grid(True)

        # Save the plot
        plot_path = os.path.join(output_dir, f'{series_name}_plot.png')
        plt.savefig(plot_path)
        plt.close()

        print(f"Plot for {series_name} saved to {plot_path}")
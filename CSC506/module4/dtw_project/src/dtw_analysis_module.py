import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from dtaidistance import dtw
from itertools import combinations
# import dtw
from dtaidistance import dtw_visualisation as dtwvis




# def perform_advanced_dtw_analysis(normalized_dfs, max_series=None, dtw_window=None):
#     series_names = list(normalized_dfs.keys())
#     if max_series is not None:
#         series_names = series_names[:max_series]
#
#     dtw_results = []
#     warping_paths = {}
#
#     for (name1, name2) in combinations(series_names, 2):
#         series1 = normalized_dfs[name1].iloc[:, 0].values
#         series2 = normalized_dfs[name2].iloc[:, 0].values
#
#         # Calculate DTW distance and warping path
#         distance, paths = dtw.warping_paths(series1, series2, window=dtw_window)
#         best_path = dtw.best_path(paths)
#
#         dtw_results.append({
#             'series1': name1,
#             'series2': name2,
#             'dtw_distance': distance
#         })
#
#         warping_paths[(name1, name2)] = {
#             'paths': paths,
#             'best_path': best_path
#         }
#
#     return pd.DataFrame(dtw_results), warping_paths


def perform_advanced_dtw_analysis(normalized_dfs, max_series=None, dtw_window=None, return_matrix=True):
    series_names = list(normalized_dfs.keys())
    if max_series is not None:
        series_names = series_names[:max_series]

    dtw_results = []
    warping_paths = {}

    for (name1, name2) in combinations(series_names, 2):
        series1 = normalized_dfs[name1].iloc[:, 0].values
        series2 = normalized_dfs[name2].iloc[:, 0].values

        # Convert series to numeric, coercing errors to NaN
        series1 = pd.to_numeric(series1, errors='coerce')
        series2 = pd.to_numeric(series2, errors='coerce')

        # Remove NaN values from NumPy arrays (if any)
        series1 = series1[~np.isnan(series1)]
        series2 = series2[~np.isnan(series2)]

        # Ensure both series are still of equal length after dropping NaNs
        min_length = min(len(series1), len(series2))
        series1 = series1[:min_length]
        series2 = series2[:min_length]

        # Calculate DTW distance and warping path
        distance, paths = dtw.warping_paths(series1, series2, window=dtw_window)
        best_path = dtw.best_path(paths)

        dtw_results.append({
            'series1': name1,
            'series2': name2,
            'dtw_distance': distance
        })

        warping_paths[(name1, name2)] = {
            'paths': paths,
            'best_path': best_path
        }

    results_df = pd.DataFrame(dtw_results)

    if return_matrix:
        # Create a distance matrix
        n = len(series_names)
        distance_matrix = np.zeros((n, n))
        for _, row in results_df.iterrows():
            i = series_names.index(row['series1'])
            j = series_names.index(row['series2'])
            distance_matrix[i, j] = distance_matrix[j, i] = row['dtw_distance']

        return results_df, warping_paths, distance_matrix
    else:
        return results_df, warping_paths



# def plot_dtw_matrix(dtw_results, series_names, output_dir='plots/dtw_analysis'):
#     """
#     Plot the DTW distance matrix.
#
#     :param dtw_results: DataFrame with DTW distances
#     :param series_names: List of series names
#     :param output_dir: Directory to save the plot
#     """
#     os.makedirs(output_dir, exist_ok=True)
#
#     n = len(series_names)
#     distance_matrix = np.zeros((n, n))
#
#     for _, row in dtw_results.iterrows():
#         i = series_names.index(row['series1'])
#         j = series_names.index(row['series2'])
#         distance_matrix[i, j] = distance_matrix[j, i] = row['dtw_distance']
#
#     plt.figure(figsize=(12, 10))
#     plt.imshow(distance_matrix, cmap='viridis')
#     plt.colorbar(label='DTW Distance')
#     plt.xticks(range(n), series_names, rotation=90)
#     plt.yticks(range(n), series_names)
#     plt.title('DTW Distance Matrix')
#     plt.tight_layout()
#
#     plot_path = os.path.join(output_dir, 'dtw_distance_matrix.png')
#     plt.savefig(plot_path)
#     plt.close()
#
#     print(f"DTW distance matrix plot saved to {plot_path}")



import os
import numpy as np
import matplotlib.pyplot as plt

def plot_dtw_matrix(dtw_results, series_names, output_dir='plots/dtw_analysis', distance_matrix=None):
    """
    Plot the DTW distance matrix.

    :param dtw_results: DataFrame with DTW distances or tuple containing (DataFrame, warping_paths, distance_matrix)
    :param series_names: List of series names
    :param output_dir: Directory to save the plot
    :param distance_matrix: Pre-calculated distance matrix (optional)
    """
    os.makedirs(output_dir, exist_ok=True)

    # Handle case where dtw_results is a tuple
    if isinstance(dtw_results, tuple):
        if len(dtw_results) == 3:
            dtw_results, _, distance_matrix = dtw_results
        else:
            dtw_results, _ = dtw_results

    n = len(series_names)

    # If distance_matrix is not provided, calculate it from dtw_results
    if distance_matrix is None:
        distance_matrix = np.zeros((n, n))
        for _, row in dtw_results.iterrows():
            i = series_names.index(row['series1'])
            j = series_names.index(row['series2'])
            distance_matrix[i, j] = distance_matrix[j, i] = row['dtw_distance']

    plt.figure(figsize=(12, 10))
    plt.imshow(distance_matrix, cmap='viridis')
    plt.colorbar(label='DTW Distance')
    plt.xticks(range(n), series_names, rotation=90)
    plt.yticks(range(n), series_names)
    plt.title('DTW Distance Matrix')
    plt.tight_layout()

    plot_path = os.path.join(output_dir, 'dtw_distance_matrix.png')
    plt.savefig(plot_path)
    plt.close()

    print(f"DTW distance matrix plot saved to {plot_path}")


def plot_warping_path(series1, series2, path, name1, name2, output_dir='plots/dtw_analysis'):
    """
    Plot the warping path for two time series.
    :param series1: First time series
    :param series2: Second time series
    :param path: Warping path
    :param name1: Name of the first series
    :param name2: Name of the second series
    :param output_dir: Directory to save the plot
    """
    # fig, ax = plt.subplots(figsize=(12, 8))
    # dtwvis.plot_warping(series1, series2, path, fig=fig, ax=ax)
    # plt.title(f"DTW Warping Path: {name1} vs {name2}")
    # plt.tight_layout()
    # plt.savefig(f"{output_dir}/warping_path_{name1}_vs_{name2}.png")
    # plt.close()

    os.makedirs(output_dir, exist_ok=True)

    # Create a new figure
    fig, axs = plt.subplots(1, 2, figsize=(16, 8))

    # Plot the warping using dtwvis
    dtwvis.plot_warping(series1, series2, path, filename=None, fig=fig, axs=axs)

    # Customize the plot
    fig.suptitle(f'Warping Path: {name1} vs {name2}')
    axs[0].set_xlabel(name1)
    axs[0].set_ylabel(name2)
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Value')

    # Save the plot
    plot_path = os.path.join(output_dir, f'warping_path_{name1}_vs_{name2}.png')
    plt.savefig(plot_path)
    plt.close(fig)

    print(f"Warping path plot saved to {plot_path}")

# def analyze_warping_shape(path, name1, name2):
#     path_array = np.array(path)
#     diagonal = np.linspace(0, len(path) - 1, len(path))
#     deviation = path_array[:, 0] - diagonal
#
#     lead_lag = "leads" if np.mean(deviation) > 0 else "lags"
#     max_deviation = np.max(np.abs(deviation))
#
#     print(f"Warping shape analysis for {name1} vs {name2}:")
#     print(f"  - {name1} generally {lead_lag} {name2}")
#     print(f"  - Maximum temporal deviation: {max_deviation:.2f} time steps")


def analyze_warping_shape(path, name1, name2):
    path_array = np.array(path, dtype=float)

    if path_array.ndim == 1 or path_array.shape[1] != 2:
        raise ValueError(f"Expected 2D path array with two columns, got shape {path_array.shape}")

    diagonal = np.linspace(0, len(path_array) - 1, len(path_array))

    # Now calculate deviation safely
    deviation = path_array[:, 0] - diagonal

    lead_lag = "leads" if np.mean(deviation) > 0 else "lags"
    max_deviation = np.max(np.abs(deviation))

    print(f"Warping shape analysis for {name1} vs {name2}:")
    print(f"  - {name1} generally {lead_lag} {name2}")
    print(f"  - Maximum temporal deviation: {max_deviation:.2f} time steps")


# def find_subsequence_matches(series1, series2, threshold, name1, name2):
#     # Ensure series are 1D numpy arrays
#     # s1 = np.array(series1).reshape(-1)
#     # s2 = np.array(series2).reshape(-1)
#
#     s1 = np.array(series1, dtype=np.float64).reshape(-1)
#     s2 = np.array(series2, dtype=np.float64).reshape(-1)
#
#     # Calculate the distance matrix
#     # matrix = dtw.distance_matrix(s1, s2)
#    #  matrix = dtw.distance_matrix_fast(s1[np.newaxis, :], s2[np.newaxis, :])
#     # matrix = dtw.distance_matrix_warping_path(s1, s2)
#     matrix = dtw.dtw_ndim.distance_matrix_fast(s1, s2)
#
#    #  matrix = dtw.distance_matrix_fast(series1, series2)
#
#     # Find matches below the threshold
#     matches = np.where(matrix < threshold)
#
#     print(f"Subsequence matches for {name1} vs {name2} (threshold = {threshold}):")
#     for i, j in zip(matches[0], matches[1]):
#         print(f"  - Match at {name1}[{i}] and {name2}[{j}]")
#     else:
#         print("  No subsequence matches found below the threshold.")
#
#     # Printing the overall DTW distance:
#     overall_distance = matrix[0, 0]
#     print(f"Overall DTW distance between {name1} and {name2}: {overall_distance}")


def find_subsequence_matches(series1, series2, threshold, name1, name2):
    # Ensure series are 1D numpy arrays
    s1 = np.array(series1, dtype=np.float64).reshape(-1)
    s2 = np.array(series2, dtype=np.float64).reshape(-1)
    print(f"{s1=}")
    print(f"{s2=}")
    print(f"{series1=}")
    print(f"{series1=}")

    print(f"{[s1]=}")
    print(f"{[s2]=}")

    # Calculate the DTW distance matrix
    # matrix = dtw.distance_matrix_fast([s1], [s2])
    matrix = dtw.distance_matrix_fast([s1, s2], compact=False)

    # Find matches below the threshold
    matches = np.where(matrix < threshold)

    print(f"Subsequence matches for {name1} vs {name2} (threshold = {threshold}):")
    if matches[0].size > 0:
        for i, j in zip(matches[0], matches[1]):
            print(f"  - Match at {name1}[{i}] and {name2}[{j}]")
    else:
        print("  No subsequence matches found below the threshold.")

    # Printing the overall DTW distance:
    overall_distance = matrix[0, 0]
    print(f"Overall DTW distance between {name1} and {name2}: {overall_distance}")





# Analyze and visualize warping paths
def analyze_and_visualize_warping_paths(normalized_dfs, warping_paths, threshold=0.1, output_dir='plots/dtw_analysis'):
    """
    Analyze and visualize warping paths for all pairs of time series.

    :param normalized_dfs: Dictionary of normalized DataFrames
    :param warping_paths: Dictionary of warping paths for each pair of series
    :param threshold: Threshold for subsequence matching
    :param output_dir: Directory to save output plots
    """
    for (name1, name2), wp in warping_paths.items():
        print(f"Analyzing {name1} vs {name2}")
        if 'best_path' not in wp or len(wp['best_path']) == 0:
            print(f"Warning: No best_path found for {name1} vs {name2}")
            continue



        series1 = normalized_dfs[name1].iloc[:, 0].values
        series2 = normalized_dfs[name2].iloc[:, 0].values

        # Plot warping path
        plot_warping_path(series1, series2, wp['best_path'], name1, name2, output_dir)

        # Analyze warping shape
        analyze_warping_shape(wp['best_path'], name1, name2)
        print(f"{wp['best_path']=}")

        # Find subsequence matches
        find_subsequence_matches(series1, series2, threshold, name1, name2)

        print("\n" + "-" * 50 + "\n")  # Separator between analyses

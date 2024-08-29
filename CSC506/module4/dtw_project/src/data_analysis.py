import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

# def analyze_dtw_results(file_path):
#     # Print current working directory
#     print(f"Current working directory: {os.getcwd()}")
#     # Print the file path to be read
#     print(f"Reading file from path: {file_path}")
#
#     df = pd.read_csv(file_path)
#
#     # Basic statistics
#     print("DTW Distance Statistics:")
#     print(df['dtw_distance'].describe())
#
#     # Histogram of DTW distances
#     plt.figure(figsize=(10, 6))
#     plt.hist(df['dtw_distance'], bins=20)
#     plt.title('Distribution of DTW Distances')
#     plt.xlabel('DTW Distance')
#     plt.ylabel('Frequency')
#     plt.savefig('plots/output_analysis/dtw_distance_distribution.png')
#     plt.close()
#
#     # Clustering of time series based on DTW distances
#     X = df['dtw_distance'].values.reshape(-1, 1)
#     kmeans = KMeans(n_clusters=3, random_state=42)
#     df['cluster'] = kmeans.fit_predict(X)
#
#     # Visualize clusters
#     plt.figure(figsize=(10, 6))
#     for i in range(3):
#         cluster_data = df[df['cluster'] == i]
#         plt.scatter(cluster_data.index, cluster_data['dtw_distance'], label=f'Cluster {i}')
#     plt.title('Clustering of Time Series based on DTW Distances')
#     plt.xlabel('Pair Index')
#     plt.ylabel('DTW Distance')
#     plt.legend()
#     plt.savefig('plots/output_analysis/dtw_clusters.png')
#     plt.close()
#
#     # Identify most similar and dissimilar pairs
#     most_similar = df.loc[df['dtw_distance'].idxmin()]
#     most_dissimilar = df.loc[df['dtw_distance'].idxmax()]
#
#     print("\nMost Similar Pair:")
#     print(f"{most_similar['series1']} and {most_similar['series2']} with DTW distance: {most_similar['dtw_distance']}")
#
#     print("\nMost Dissimilar Pair:")
#     print(
#         f"{most_dissimilar['series1']} and {most_dissimilar['series2']} with DTW distance: {most_dissimilar['dtw_distance']}")


# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans


def analyze_dtw_results(file_path):
    df = pd.read_csv(file_path)

    # Basic statistics
    print("DTW Distance Statistics:")
    print(df['dtw_distance'].describe())

    # Histogram of DTW distances
    plt.figure(figsize=(10, 6))
    plt.hist(df['dtw_distance'], bins=20)
    plt.title('Distribution of DTW Distances')
    plt.xlabel('DTW Distance')
    plt.ylabel('Frequency')
    plt.savefig('plots/output_analysis/dtw_distance_distribution.png')
    plt.close()

    # Clustering of time series based on DTW distances
    X = df['dtw_distance'].values.reshape(-1, 1)

    if len(X) >= 3:  # Only proceed if there are at least 3 samples
        kmeans = KMeans(n_clusters=3, random_state=42)
        df['cluster'] = kmeans.fit_predict(X)

        # Visualize clusters
        plt.figure(figsize=(10, 6))
        for i in range(3):
            cluster_data = df[df['cluster'] == i]
            plt.scatter(cluster_data.index, cluster_data['dtw_distance'], label=f'Cluster {i}')
        plt.title('Clustering of Time Series based on DTW Distances')
        plt.xlabel('Pair Index')
        plt.ylabel('DTW Distance')
        plt.legend()
        plt.savefig('plots/output_analysis/dtw_clusters.png')
        plt.close()
    else:
        print("Not enough samples to perform clustering. Need at least 3 samples.")

    # Identify most similar and dissimilar pairs
    if not df.empty:
        most_similar = df.loc[df['dtw_distance'].idxmin()]
        most_dissimilar = df.loc[df['dtw_distance'].idxmax()]

        print("\nMost Similar Pair:")
        print(
            f"{most_similar['series1']} and {most_similar['series2']} with DTW distance: {most_similar['dtw_distance']}")

        print("\nMost Dissimilar Pair:")
        print(
            f"{most_dissimilar['series1']} and {most_dissimilar['series2']} with DTW distance: {most_dissimilar['dtw_distance']}")

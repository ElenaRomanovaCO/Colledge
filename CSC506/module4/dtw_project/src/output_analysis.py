import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def gather_output(dtw_results, time_series_data):
    output = []
    for _, row in dtw_results.iterrows():
        series1 = time_series_data[row['series1']]
        series2 = time_series_data[row['series2']]
        output.append({
            'series1': row['series1'],
            'series2': row['series2'],
            'dtw_distance': row['dtw_distance'],
            'series1_mean': series1.mean(),
            'series2_mean': series2.mean(),
            'series1_std': series1.std(),
            'series2_std': series2.std(),
            'correlation': series1.corr(series2)
        })
    return pd.DataFrame(output)


def analyze_output(output_file):
    df = pd.read_csv(output_file)

    # Create a correlation heatmap
    plt.figure(figsize=(10, 8))
    corr_matrix = df[
        ['dtw_distance', 'series1_mean', 'series2_mean', 'series1_std', 'series2_std', 'correlation']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap of Output Variables')
    plt.tight_layout()
    plt.savefig('plots/output_analysis/output_correlation_heatmap.png')
    plt.close()

    # Create a scatter plot of DTW distance vs correlation
    plt.figure(figsize=(10, 6))
    plt.scatter(df['correlation'], df['dtw_distance'])
    plt.xlabel('Correlation')
    plt.ylabel('DTW Distance')
    plt.title('DTW Distance vs Correlation')
    plt.savefig('plots/output_analysis/dtw_vs_correlation_scatter.png')
    plt.close()

    print("Output analysis complete. New plots saved in the 'plots/output_analysis' directory.")
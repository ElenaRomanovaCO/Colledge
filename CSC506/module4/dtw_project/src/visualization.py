import matplotlib.pyplot as plt
import numpy as np
import os

def plot_time_series(data, title=None, filename=None):
    plt.figure(figsize=(12, 6))
    plt.plot(data)
    plt.xlabel('Time')
    plt.ylabel('Value')
    if title:
        plt.title(title)
    if filename:
        plt.savefig(filename)
    plt.close()

def plot_dtw_result(s1, s2, path, title=None, filename=None):
    plt.figure(figsize=(12, 8))
    plt.plot(s1, label='Series 1')
    plt.plot(s2, label='Series 2')
    for i, j in path:
        plt.plot([i, j], [s1[i], s2[j]], 'r-', alpha=0.3)
    plt.legend()
    if title:
        plt.title(title)
    if filename:
        plt.savefig(filename)
    plt.close()

# def plot_decomposed_time_series(decomposed, title=None, filename=None):
#     plt.figure(figsize=(12, 10))
#     plt.subplot(411)
#     plt.plot(decomposed['observed'])
#     plt.title('Original Time Series')
#     plt.subplot(412)
#     plt.plot(decomposed['trend'])
#     plt.title('Trend')
#     plt.subplot(413)
#     plt.plot(decomposed['seasonal'])
#     plt.title('Seasonal')
#     plt.subplot(414)
#     plt.plot(decomposed['residual'])
#     plt.title('Residual')
#     plt.tight_layout()
#     if title:
#         plt.suptitle(title)
#     if filename:
#         plt.savefig(filename)
#     plt.close()


def plot_decomposed_time_series(decomposed, title, filename):
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 12))
    decomposed.observed.plot(ax=ax1)
    ax1.set_title('Observed')
    decomposed.trend.plot(ax=ax2)
    ax2.set_title('Trend')
    decomposed.seasonal.plot(ax=ax3)
    ax3.set_title('Seasonal')
    decomposed.resid.plot(ax=ax4)
    ax4.set_title('Residual')

    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
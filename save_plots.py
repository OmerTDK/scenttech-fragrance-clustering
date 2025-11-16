"""
Script to save key plots from the fragrance clustering analysis
Run this after executing the main notebook to save visualizations as images
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
import os

# Create images directory if it doesn't exist
os.makedirs('images/plots', exist_ok=True)

# Set style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)
plt.rcParams["axes.titlesize"] = 12
plt.rcParams["axes.labelsize"] = 11
plt.rcParams["figure.dpi"] = 100

def save_current_plot(filename, dpi=150):
    """Save the current matplotlib figure"""
    plt.savefig(f'images/plots/{filename}', dpi=dpi, bbox_inches='tight')
    print(f"Saved: images/plots/{filename}")

# Example usage (uncomment and modify based on your notebook variables):
# Make sure to run your notebook first, then copy the relevant plotting code here

# Example for silhouette plot:
# plt.figure(figsize=(6, 4))
# plt.plot(kmeans_results["k"], kmeans_results["silhouette"], marker="o")
# plt.title("Silhouette score for different numbers of clusters (K-Means)")
# plt.xlabel("Number of clusters (k)")
# plt.ylabel("Silhouette score")
# save_current_plot('silhouette_analysis.png')
# plt.show()

print("Plot saving script created!")
print("To use:")
print("1. Run your notebook first to generate all plots")
print("2. For each plot you want to save, add the plotting code above")
print("3. Call save_current_plot('filename.png') before plt.show()")
print("4. Or use plt.savefig('images/plots/filename.png', dpi=150, bbox_inches='tight')")

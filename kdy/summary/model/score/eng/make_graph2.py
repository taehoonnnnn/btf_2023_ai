# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV file
df = pd.read_csv('averages.csv')

# Extract the required data
description = df['description']

# List of statistics
statistics = ['min', 'max', 'mean', 'std']

# Loop through the statistics
for stat in statistics:
    # Extract the required data for each statistic
    glove_stat = df[f'GloVe_{stat}']
    fasttext_stat = df[f'FastText_{stat}']
    use_stat = df[f'USE_{stat}']
    sbert_stat = df[f'SBERT_{stat}']
    
    # Create the plot with different colors and move the legend outside the plot
    plt.figure(figsize=(10,6))
    plt.plot(description, glove_stat, marker='o', color='blue', label='GloVe', alpha=0.7)
    plt.plot(description, fasttext_stat, marker='o', color='green', label='FastText', alpha=0.7)
    plt.plot(description, use_stat, marker='o', color='red', label='USE', alpha=0.7)
    plt.plot(description, sbert_stat, marker='o', color='purple', label='SBERT', alpha=0.7)
    
    # Annotate the actual value for each point
    for i, val in enumerate(glove_stat):
        plt.text(i, val, f' {val:.2f}', verticalalignment='bottom', fontsize=9)
    for i, val in enumerate(fasttext_stat):
        plt.text(i, val, f' {val:.2f}', verticalalignment='bottom', fontsize=9)
    for i, val in enumerate(use_stat):
        plt.text(i, val, f' {val:.2f}', verticalalignment='bottom', fontsize=9)
    for i, val in enumerate(sbert_stat):
        plt.text(i, val, f' {val:.2f}', verticalalignment='bottom', fontsize=9)
    
    # Add labels and move the legend outside the plot
    plt.xlabel('Description')
    plt.ylabel(f'{stat.capitalize()} Score')
    plt.title(f'Comparison of {stat.capitalize()} Scores')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Display the plot
    plt.tight_layout()
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the csv file
df = pd.read_csv('averages.csv')

# Filter the DataFrame to only include the specified descriptions
df_filtered = df[df['description'].isin(['default','frequency_penalty_-2','frequency_penalty_-1','frequency_penalty_1', 'frequency_penalty_2' ])]

# Select the desired columns
df_selected = df_filtered[['description', 'GloVe_min','GloVe_max','GloVe_mean','GloVe_std','FastText_min','FastText_max','FastText_mean','FastText_std','USE_min','USE_max','USE_mean','USE_std','SBERT_min','SBERT_max','SBERT_mean','SBERT_std']]

# Set the description column as the index for better plotting
df_selected.set_index('description', inplace=True)

# Separate the std and non-std columns
df_std = df_selected.filter(regex='std$', axis=1)
df_non_std = df_selected.filter(regex='^(?!.*std).*$')

# Set up the subplots
fig, ax = plt.subplots(2, 1, figsize=(15, 20))

# Plot non-std values
df_non_std.plot(kind='bar', colormap='viridis', ax=ax[0])
ax[0].set_title('Comparison of Keyword and Keyword_nltk Metrics (Min, Max, Mean) for temperature_0, default, temperature_2')
ax[0].set_ylabel('Values')
ax[0].set_xlabel('Description')
ax[0].legend(loc='upper left', bbox_to_anchor=(1, 1))
ax[0].set_xticks(range(len(df_non_std)))
ax[0].set_xticklabels(df_non_std.index, rotation=45)

# Add value labels to the non-std bars
for container in ax[0].containers:
    ax[0].bar_label(container, fmt='%.2f')

# Plot std values
df_std.plot(kind='bar', colormap='viridis', ax=ax[1])
ax[1].set_title('Comparison of Keyword and Keyword_nltk Metrics (Std) for temperature_0, default, temperature_2')
ax[1].set_ylabel('Values')
ax[1].set_xlabel('Description')
ax[1].legend(loc='upper left', bbox_to_anchor=(1, 1))
ax[1].set_xticks(range(len(df_std)))
ax[1].set_xticklabels(df_std.index, rotation=45)

# Add value labels to the std bars
for container in ax[1].containers:
    ax[1].bar_label(container, fmt='%.2f')

# Adjust layout
plt.tight_layout()
plt.show()

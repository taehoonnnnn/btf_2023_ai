import pandas as pd
from nltk.translate.bleu_score import sentence_bleu

# load the csv file
df = pd.read_csv('output.csv', header=None)

# ensure that the reference and candidate columns are string type
assert df[0].dtype == object and df[1].dtype == object

# split the sentences into words
df[0] = df[0].apply(lambda x: x.split())
df[1] = df[1].apply(lambda x: x.split())

# calculate the BLEU score for each row and store it in a new column
df['bleu'] = df.apply(lambda row: sentence_bleu([row[0]], row[1], weights=(1, 0, 0, 0)), axis=1)

# print BLEU scores
print("BLEU scores per row:")
print(df['bleu'])

# calculate and print the average BLEU score
average_bleu = df['bleu'].mean()
print("Average BLEU score:", average_bleu)

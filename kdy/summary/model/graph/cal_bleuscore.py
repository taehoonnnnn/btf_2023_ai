import pandas as pd
from nltk.translate.bleu_score import sentence_bleu

# load the csv file
df = pd.read_csv('output_gpt-3.5-turbo.csv', header=0)

# ensure that the reference columns are string type
assert df.iloc[:, 1].dtype == object

# split the sentences into words
df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: x.split())
for i in range(2, df.shape[1]):
    assert df.iloc[:, i].dtype == object
    df.iloc[:, i] = df.iloc[:, i].apply(lambda x: x.split())

# calculate the BLEU score for each row and store it in a new dataframe
def calc_bleu(row):
    reference = row[1]
    candidates = row[2:]
    scores = [sentence_bleu([reference], candidate, weights=(1, 0, 0, 0)) for candidate in candidates]
    return scores  # return list of scores for this row

bleu_scores = df.apply(calc_bleu, axis=1)  # returns a series of lists
df_bleu = pd.DataFrame(bleu_scores.tolist())  # convert to dataframe

# Set column names from original dataframe
df_bleu.columns = df.columns[2:]

# print BLEU scores
print("BLEU scores per row:")
print(df_bleu)

df_bleu.to_csv('bleuscore.csv',index=False, encoding="utf-8")

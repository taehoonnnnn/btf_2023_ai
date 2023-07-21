import pandas as pd

def compute_score(response, keywords):
    score = sum([1 if keyword in response else 0 for keyword in keywords])
    return score

def main():
    # Load the data
    data = pd.read_csv('자본시장_금융.csv')

    # Apply the function to each row of the DataFrame
    score_keyword = data.apply(lambda row: compute_score(row['response'], 
                                [row['keyword1_trans'], row['keyword2_trans'], row['keyword3_trans'], 
                                 row['keyword4_trans'], row['keyword5_trans']]), axis=1)

    data.insert(1, 'score_keyword', score_keyword)

    data.to_csv('output.csv', index=False)


if __name__ == "__main__":
    main()

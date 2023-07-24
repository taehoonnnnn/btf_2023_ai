import pandas as pd

def compute_score(response, keywords):
    score = sum([1 if keyword in response else 0 for keyword in keywords])
    return score

def main():
    # Load the data
    data = pd.read_csv('자본시장_금융_kor.csv')

    # Apply the function to each row of the DataFrame
    score_keyword = data.apply(lambda row: compute_score(row['response'], 
                                [row['keyword1'], row['keyword2'], row['keyword3'], 
                                 row['keyword4'], row['keyword5']]), axis=1)

    data.insert(1, 'score_keyword', score_keyword)

    data.to_csv('add_1_keyword.csv', index=False)


if __name__ == "__main__":
    main()

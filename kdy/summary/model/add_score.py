import pandas as pd

def compute_score(response, keywords):
    score = sum([1 if keyword in response else 0 for keyword in keywords])
    return score

def main():
    # Load the data
    data = pd.read_csv('output.csv')

    # Apply the function to each row of the DataFrame
    data['score'] = data.apply(lambda row: compute_score(row['response'], 
                                                         [row['keyword1'], row['keyword2'], row['keyword3'], row['keyword4'], row['keyword5']]), axis=1)

    # Save the updated DataFrame to a new CSV file
    data.to_csv('output2.csv', index=False)


if __name__ == "__main__":
    main()
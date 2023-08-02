import pandas as pd
import konlpy 
from konlpy.tag import Okt

def compute_score(response, keywords):
    # 형태소 분석기 초기화
    okt = Okt()

    # response를 형태소로 분리
    response_morphs = okt.morphs(response)

    # 키워드 점수 초기화
    keyword_scores = {keyword: 0 for keyword in keywords}

    # 각 형태소가 키워드에 포함되는지 확인하고, 포함되면 해당 키워드의 점수 증가
    for morph in response_morphs:
        for keyword in keywords:
            if morph in keyword:
                keyword_scores[keyword] += 1

    # keyword_scores의 평균값 계산
    average_score = sum(keyword_scores.values()) / len(keyword_scores)

    return average_score

def main():
    # Load the data
    data = pd.read_csv('add_6_koelectra.csv')

    # Apply the function to each row of the DataFrame
    score_keyword = data.apply(lambda row: compute_score(row['response'], 
                                [row['keyword1'], row['keyword2'], row['keyword3'], 
                                 row['keyword4'], row['keyword5']]), axis=1)

    data.insert(1, 'keyword_konlpy', score_keyword)

    data.to_csv('add_7_keyword_konlpy.csv', index=False)

if __name__ == "__main__":
    main()

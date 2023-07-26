import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# NLTK의 Stopwords를 다운로드 받습니다.
import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')

def compute_score(response, keywords):
    # Stop words 및 형태소 분석기(lemmatizer) 초기화
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # response를 형태소로 분리
    response_morphs = word_tokenize(response)

    # Stop words 제거 및 lemmatization
    response_morphs = [lemmatizer.lemmatize(w) for w in response_morphs if not w in stop_words]
    
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
    data = pd.read_csv('add_5_glove.csv')

    # Apply the function to each row of the DataFrame
    score_keyword = data.apply(lambda row: compute_score(row['response'], 
                                [row['keyword1_trans'], row['keyword2_trans'], row['keyword3_trans'], 
                                 row['keyword4_trans'], row['keyword5_trans']]), axis=1)

    data.insert(1, 'score_keyword_nltk', score_keyword)

    data.to_csv('add_6_keyword_nltk.csv', index=False)

if __name__ == "__main__":
    main()

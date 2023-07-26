import pandas as pd
import os

# csv 파일 불러오기
df = pd.read_csv('add_6_keyword_nltk.csv')

# 각 컬럼의 최솟값, 최댓값, 평균, 표준편차 계산하기
columns = ['GloVe', 'FastText', 'USE', 'SBERT', 'score_keyword', 'score_keyword_nltk', 'response']
stats = ['min', 'max', 'mean', 'std']

data = {"description": ["영어 default"]}

for col in columns:
    if col == 'response':
        len_response = df[col].str.len()
        data.update({
            f"{col}_min": len_response.min(),
            f"{col}_max": len_response.max(),
            f"{col}_mean": len_response.mean(),
            f"{col}_std": len_response.std(),
        })
    else:
        data.update({
            f"{col}_min": df[col].min(),
            f"{col}_max": df[col].max(),
            f"{col}_mean": df[col].mean(),
            f"{col}_std": df[col].std(),
        })

# 결과를 데이터 프레임으로 저장
df_mean = pd.DataFrame(data)

# 파일이 존재하는지 확인
file_exists = os.path.isfile('averages.csv')

# 데이터 프레임을 CSV 파일로 저장
# 파일이 존재하면, 헤더를 쓰지 않고 ('header=False') 추가 모드로 ('mode='a'') 저장
# 파일이 존재하지 않으면, 헤더를 쓰고 ('header=True') 새 파일로 ('mode='w'') 저장
df_mean.to_csv('averages.csv', mode='a' if file_exists else 'w', header=not file_exists, index=False)

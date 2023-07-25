import pandas as pd

# csv 파일 불러오기
df = pd.read_csv('add_5_glove.csv')

column_name_1 = df.columns[1]
column_name_2 = df.columns[2]
column_name_3 = df.columns[3]
column_name_4 = df.columns[4]
column_name_5 = df.columns[5]

# 각 컬럼의 평균 계산하기
glove = df[column_name_1].mean()
fasttext = df[column_name_2].mean()
use = df[column_name_3].mean()
sbert = df[column_name_4].mean()
keyword = df[column_name_5].mean()

# 결과를 데이터 프레임으로 저장
df_mean = pd.DataFrame({
    "description": ["영어 default"],
    column_name_1: [glove],
    column_name_2: [fasttext],
    column_name_3: [use],
    column_name_4: [sbert],
    column_name_5: [keyword],
})

# 데이터 프레임을 CSV 파일로 저장
df_mean.to_csv('averages.csv', mode='a', header=False, index=False)

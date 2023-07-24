import pandas as pd

# csv 파일 불러오기
df = pd.read_csv('add_6_koelectra.csv')

column_name_1 = df.columns[1]
column_name_2 = df.columns[2]
column_name_3 = df.columns[3]
column_name_4 = df.columns[4]
column_name_5 = df.columns[5]
column_name_6 = df.columns[6]

# 각 컬럼의 평균 계산하기
koelectra = df[column_name_1].mean()
kobert = df[column_name_2].mean()
fasttext = df[column_name_3].mean()
use = df[column_name_4].mean()
sbert = df[column_name_5].mean()
keyword = df[column_name_6].mean()

# 결과를 데이터 프레임으로 저장
df_mean = pd.DataFrame({
    "description": ["한국어 default"],
    column_name_1: [koelectra],
    column_name_2: [kobert],
    column_name_3: [fasttext],
    column_name_4: [use],
    column_name_5: [sbert],
    column_name_6: [keyword],
})

# 데이터 프레임을 CSV 파일로 저장
df_mean.to_csv('averages.csv', mode='a', header=False, index=False)

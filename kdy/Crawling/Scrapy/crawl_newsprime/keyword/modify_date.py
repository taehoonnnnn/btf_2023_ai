import pandas as pd

# csv 파일 로드
df = pd.read_csv('자본시장_금융.csv')

# 6번째 열 이름 저장
column_6_name = df.columns[5]

# 6번째 열 데이터를 쉼표(',')로 분리
split_data = df.iloc[:, 5].str.split(',', expand=True)

# 새로운 열 이름 설정
new_columns = {i: f'column_{i+6}' for i in split_data.columns}

# 데이터프레임에 새로운 열 추가
df = pd.concat([df, split_data.rename(columns=new_columns)], axis=1)

# 원래의 6번째 열 삭제
df = df.drop(column_6_name, axis=1)

# csv 파일로 저장
df.to_csv('자본시장_금융2.csv', index=False)

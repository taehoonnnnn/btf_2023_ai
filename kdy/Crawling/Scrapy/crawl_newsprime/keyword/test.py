import pandas as pd

# 파일 로드
df = pd.read_csv('자본시장_금융2.csv')

# 4번째 열을 날짜형식으로 변환하고, 원하는 형식으로 바꾸기
df.iloc[:, 3] = pd.to_datetime(df.iloc[:, 3]).dt.strftime('%Y.%m.%d')

# 변형된 데이터프레임을 새로운 파일로 저장
df.to_csv('new_file.csv', index=False)

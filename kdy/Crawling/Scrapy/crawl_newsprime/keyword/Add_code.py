import pandas as pd

# csv 파일 불러오기
df = pd.read_csv('자본시장_금융.csv')

# 새로운 열 추가, 모든 값이 101
df['분류코드'] = 101

# 변경된 데이터프레임을 새 csv 파일로 저장
df.to_csv('new_file.csv', index=False)

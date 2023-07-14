import pandas as pd

# csv 파일 불러오기
data = pd.read_csv('자본시장_금융.csv', header=None)

# 4번째 열을 기준으로 정렬
sorted_data = data.sort_values(by=3, ascending=False)

# 정렬된 데이터 저장
sorted_data.to_csv('sorted_file.csv', index=False)

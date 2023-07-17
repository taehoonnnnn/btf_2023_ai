import pandas as pd

# CSV 파일을 읽어옵니다.
df = pd.read_csv('자본시장_금융.csv')

# 5번째 열에서 "[프라임경제]" 부분을 제거합니다.
# 이 때, 열의 인덱스는 0부터 시작하므로 'df.columns[4]' 를 사용합니다.
df[df.columns[4]] = df[df.columns[4]].str.replace("[프라임경제]", "", regex=False)

# 결과를 새 CSV 파일로 저장합니다.
df.to_csv('자본시장_금융1.csv', index=False)

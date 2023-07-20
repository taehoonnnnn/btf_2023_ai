import pandas as pd

# CSV 파일을 읽습니다
df1 = pd.read_csv('자본시장_금융.csv')
df2 = pd.read_csv('자본시장_금융_default.csv')

# df1에서 'content' 열을 복사합니다
new_content = df1['content'].copy()

# df2에 'new_content'라는 새로운 열을 만들어서 복사한 'content'를 추가합니다
df2['content'] = new_content

# 변경된 df2를 새로운 CSV 파일로 저장합니다
df2.to_csv('자본시장_금융_default_new.csv', index=False)

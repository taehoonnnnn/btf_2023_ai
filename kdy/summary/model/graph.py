import pandas as pd
import matplotlib.pyplot as plt

# 데이터를 CSV 파일로부터 읽기
df = pd.read_csv('bleuscore_graph.csv')

# 평균 점수 계산
average_scores = df.mean()

# 막대 그래프 그리기
plt.figure(figsize=(12,6))
plt.bar(average_scores.index, average_scores.values)
plt.title('Average Bleu Scores')
plt.ylabel('Average Score')
plt.xlabel('Configuration')
plt.xticks(rotation=30)  # X 축 레이블 회전 - 긴 이름을 위해
plt.tight_layout()  # 그래프 레이아웃 조정
plt.show()

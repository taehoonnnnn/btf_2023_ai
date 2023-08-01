import pandas as pd
import matplotlib.pyplot as plt

# 로컬 파일 경로를 지정합니다.
# 이 경로는 사용자의 환경에 따라 변경해야 합니다.
file_path = '기타\output_fewshot.csv'

# CSV 파일을 읽어옵니다.
data = pd.read_csv(file_path)

# 점수들의 리스트를 만듭니다.
scores = ['score_keyword_nltk', 'GloVe', 'FastText', 'USE', 'SBERT', 'score_keyword']

# 플롯을 위한 서브플롯 그리드를 생성합니다.
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))

# axs 배열을 1차원으로 바꿉니다.
axs = axs.flatten()

# 각 점수에 대해 히스토그램을 그립니다.
for ax, score in zip(axs, scores):
    # 히스토그램을 그립니다.
    data[score].hist(bins=30, ax=ax, color='skyblue', edgecolor='black')
    # 서브플롯의 제목을 설정합니다.
    ax.set_title(f'Distribution of {score} scores')

# 레이아웃을 조정합니다.
plt.tight_layout()

# 플롯을 보여줍니다.
plt.show()

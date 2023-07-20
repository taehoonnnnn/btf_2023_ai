from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 문장과 키워드를 정의합니다
# sentence = "국내 은행 연체율이 4월말 기준 0.37%로 32개월만에 최고 수준을 기록했다. 기업대출과 가계대출의 연체율이 상승한 것이 원인이다. 금감원은 이러한 추세가 계속될 수 있으며 건전성 관리와 손실흡수능력을 강화할 것을 약속했다."
sentence = "금감원은 이러한 추세가 계속될 수 있으며 건전성 관리와 손실흡수능력을 강화할 것을 약속했다."

keywords = ["은행권 연체율", "금융감독원", "기업 연체율", "추세 유지", "가계대출 연체율", "손실흡수능력"]

# 문장과 키워드를 하나의 리스트로 합칩니다
corpus = [sentence] + keywords

# Sentence-BERT 모델을 로드합니다
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# 문장과 키워드를 벡터로 변환합니다
embeddings = model.encode(corpus)

# 문장(첫 번째 문서)와 각 키워드 간의 코사인 유사도를 계산합니다
cosine_similarities = cosine_similarity([embeddings[0]], embeddings[1:]).flatten()

# 코사인 유사도를 점수로 변환합니다 (100점 만점)
similarity_scores = [round(i*100, 2) for i in cosine_similarities]

for keyword, score in zip(keywords, similarity_scores):
    print(f"Keyword '{keyword}' similarity score: {score}")

# 전체
# Keyword '은행권 연체율' similarity score: 74.88
# Keyword '금융감독원' similarity score: 27.99
# Keyword '기업 연체율' similarity score: 45.47
# Keyword '추세 유지' similarity score: 10.96
# Keyword '가계대출 연체율' similarity score: 76.53

# "국내 은행 연체율이 4월말 기준 0.37%로 32개월만에 최고 수준을 기록했다."
# Keyword '은행권 연체율' similarity score: 60.33
# Keyword '금융감독원' similarity score: 17.95
# Keyword '기업 연체율' similarity score: 33.75
# Keyword '추세 유지' similarity score: 0.3
# Keyword '가계대출 연체율' similarity score: 53.92

# 기업대출과 가계대출의 연체율이 상승한 것이 원인이다. 
# Keyword '은행권 연체율' similarity score: 58.61
# Keyword '금융감독원' similarity score: 22.37
# Keyword '기업 연체율' similarity score: 39.86
# Keyword '추세 유지' similarity score: 0.37
# Keyword '가계대출 연체율' similarity score: 73.22

# 금감원은 이러한 추세가 계속될 수 있으며 건전성 관리와 손실흡수능력을 강화할 것을 약속했다.
# Keyword '은행권 연체율' similarity score: 15.4
# Keyword '금융감독원' similarity score: 15.45
# Keyword '기업 연체율' similarity score: 27.44
# Keyword '추세 유지' similarity score: 40.98
# Keyword '가계대출 연체율' similarity score: 19.24

# 
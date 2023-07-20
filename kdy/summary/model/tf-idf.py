from konlpy.tag import Hannanum
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 형태소 분석기를 생성합니다
hannanum = Hannanum()

# 문장과 키워드를 정의합니다
sentence = "국내 은행 연체율이 4월말 기준 0.37%로 32개월만에 최고 수준을 기록했다. 기업대출과 가계대출의 연체율이 상승한 것이 원인이다. 금감원은 이러한 추세가 계속될 수 있으며 건전성 관리와 손실흡수능력을 강화할 것을 약속했다."
keywords = ["은행권 연체율", "금융감독원", "기업 연체율", "추세 유지", "가계대출 연체율"]

# 문장과 키워드를 형태소 분석기를 사용하여 토큰화합니다
sentence = " ".join(hannanum.morphs(sentence))
keywords = [" ".join(hannanum.morphs(keyword)) for keyword in keywords]

# 문장과 키워드를 하나의 리스트로 합칩니다
corpus = [sentence] + keywords

# TF-IDF Vectorizer 객체를 생성하고 문장과 키워드에 적용합니다
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# 문장(첫 번째 문서)와 각 키워드 간의 코사인 유사도를 계산합니다
cosine_similarities = cosine_similarity(X[0:1], X).flatten()

# 코사인 유사도를 점수로 변환합니다 (100점 만점)
similarity_scores = [round(i*100, 2) for i in cosine_similarities[1:]]

for keyword, score in zip(keywords, similarity_scores):
    print(f"Keyword '{keyword}' similarity score: {score}")

from sklearn.feature_extraction.text import TfidfVectorizer

# 예시 문서 리스트
documents = [
    "국내 은행 연체율이 4월말 기준 0.37%로 32개월만에 최고 수준을 기록했다.",
    "기업대출과 가계대출의 연체율이 상승한 것이 원인이다.",
    "금감원은 이러한 추세가 계속될 수 있으며 건전성 관리와 손실흡수능력을 강화할 것을 약속했다."
]

# TfidfVectorizer 초기화
vectorizer = TfidfVectorizer()

# 문서 리스트를 이용하여 TF-IDF 벡터 계산
tfidf_matrix = vectorizer.fit_transform(documents)

# 각 단어의 TF-IDF 출력
words = vectorizer.get_feature_names_out()
for i, doc in enumerate(tfidf_matrix.toarray()):
    print(f"Document {i + 1}")
    for word, tfidf in zip(words, doc):
        print(f"{word}: {tfidf}")

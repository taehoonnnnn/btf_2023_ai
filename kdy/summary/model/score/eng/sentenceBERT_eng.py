import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Sentence-BERT 모델을 로드합니다
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# CSV 파일을 읽습니다
df = pd.read_csv('add_1_keyword.csv')

# 각 행의 'content'와 'response'에 대한 유사성 점수를 계산합니다
similarity_scores = []
for _, row in df.iterrows():
    document = row['content_trans']
    sentence = row['response']

    # 문장과 문서를 벡터로 변환합니다
    document_embedding = model.encode([document])
    sentence_embedding = model.encode([sentence])

    # 문서와 문장 간의 코사인 유사도를 계산합니다
    similarity_score = cosine_similarity(document_embedding, sentence_embedding)
    similarity_scores.append(similarity_score[0][0])

# 'SBERT'라는 새로운 열을 만들어서 유사성 점수를 추가합니다
df.insert(1, 'SBERT', similarity_scores)

# 변경된 DataFrame을 새로운 CSV 파일로 저장합니다
df.to_csv('add_2_SBERT.csv', index=False)

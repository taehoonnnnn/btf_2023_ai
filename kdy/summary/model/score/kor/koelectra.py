import pandas as pd
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# KoELECTRA 모델과 토크나이저를 로드합니다
model_name = 'monologg/koelectra-base-v3-discriminator'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# 문장이나 문서를 벡터로 변환
def get_sentence_embedding(sentence):
    inputs = tokenizer(sentence, return_tensors='pt', truncation=True, max_length=128, padding='max_length')
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state[:, 0, :].detach().numpy()
    return embeddings

# CSV 파일을 읽습니다
df = pd.read_csv('add_5_kobert.csv')

# 각 행의 'content'와 'response'에 대한 유사성 점수를 계산합니다
similarity_scores = []
for _, row in df.iterrows():
    document = row['content']
    sentence = row['response']

    # 문장과 문서를 벡터로 변환합니다
    document_embedding = get_sentence_embedding(document)
    sentence_embedding = get_sentence_embedding(sentence)

    # 문서와 문장 간의 코사인 유사도를 계산합니다
    similarity_score = cosine_similarity(document_embedding, sentence_embedding)
    similarity_scores.append(similarity_score[0][0])

# 'KoELECTRA'라는 새로운 열을 만들어서 유사성 점수를 추가합니다
df.insert(1, 'KoELECTRA', similarity_scores)

# 변경된 DataFrame을 새로운 CSV 파일로 저장합니다
df.to_csv('add_6_koelectra.csv', index=False)

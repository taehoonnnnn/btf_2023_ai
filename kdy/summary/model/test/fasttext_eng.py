import pandas as pd
from gensim.models import FastText
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# FastText 모델 파일 경로
fasttext_model_path = 'cc.ko.300.bin'

# FastText 모델 로드
fasttext_model = FastText.load_fasttext_format(fasttext_model_path)

# 문장이나 문서를 벡터로 변환
def get_sentence_embedding(sentence):
    words = sentence.split()
    word_embeddings = [fasttext_model.wv[word] for word in words if word in fasttext_model.wv]
    if not word_embeddings:  # handle case where sentence has no words in FastText's vocabulary
        return np.zeros(fasttext_model.vector_size)
    sentence_embedding = np.mean(word_embeddings, axis=0)
    return sentence_embedding

# CSV 파일을 읽습니다
df = pd.read_csv('자본시장_금융.csv')

# 각 행의 'content'와 'response'에 대한 유사성 점수를 계산합니다
similarity_scores = []
for _, row in df.iterrows():
    document = row['content_trans']
    sentence = row['response']

    # 문장과 문서를 벡터로 변환합니다
    document_embedding = get_sentence_embedding(document)
    sentence_embedding = get_sentence_embedding(sentence)

    # 문서와 문장 간의 코사인 유사도를 계산합니다
    similarity_score = cosine_similarity([document_embedding], [sentence_embedding])
    similarity_scores.append(similarity_score[0][0])

# 'FastText'라는 새로운 열을 만들어서 유사성 점수를 추가합니다
df.insert(1, 'FastText', similarity_scores)

# 변경된 DataFrame을 새로운 CSV 파일로 저장합니다
df.to_csv('output.csv', index=False)

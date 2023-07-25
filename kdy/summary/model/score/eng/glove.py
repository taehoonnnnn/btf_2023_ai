import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import KeyedVectors
from nltk.tokenize import word_tokenize
import nltk
from gensim.scripts.glove2word2vec import glove2word2vec

nltk.download('punkt')

# GloVe 모델을 Word2Vec 형식으로 변환합니다
glove_input_file = 'glove.6B.300d.txt'
word2vec_output_file = 'glove.6B.300d.word2vec.txt'
glove2word2vec(glove_input_file, word2vec_output_file)

# 변환된 GloVe 모델을 로드합니다
glove_model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)

# CSV 파일을 읽습니다
df = pd.read_csv('add_4_fasttext.csv')

# 각 행의 'content'와 'response'에 대한 유사성 점수를 계산합니다
similarity_scores = []
for _, row in df.iterrows():
    document = row['content_trans']
    sentence = row['response']

    # 문장을 토큰화하고, 각 단어의 벡터를 얻은 후 평균을 내어 문장의 벡터를 생성합니다
    document_embedding = np.mean([glove_model[word] for word in word_tokenize(document) if word in glove_model], axis=0)
    sentence_embedding = np.mean([glove_model[word] for word in word_tokenize(sentence) if word in glove_model], axis=0)

    # 문서와 문장 간의 코사인 유사도를 계산합니다
    similarity_score = cosine_similarity([document_embedding], [sentence_embedding])
    similarity_scores.append(similarity_score[0][0])

# 'GloVe'라는 새로운 열을 만들어서 유사성 점수를 추가합니다
df.insert(1, 'GloVe', similarity_scores)

# 변경된 DataFrame을 새로운 CSV 파일로 저장합니다
df.to_csv('add_5_glove.csv', index=False)

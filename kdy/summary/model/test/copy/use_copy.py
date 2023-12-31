from absl import logging
import tensorflow as tf
import tensorflow_hub as hub
from sklearn.metrics.pairwise import cosine_similarity

# 문장과 문서를 정의합니다
document = "보람상조가 플랫폼 기업과 함께 상품 판매채널을 확대한다. 더 많은 경험을 소비자에게 제공해 고객만족 경영에 한걸음 다가서기 위한 적극적인 행보로 풀이된다.7일 보람그룹에 따르면 상조계열사 보람상조플러스는 플랫폼 기업 비즈마켓(구 인터파크비즈마켓), 가구구독 기업 이해라이프스타일과 3자 간 B2B 업무협약을 맺었다. 비즈마켓이 운영하는 2000여 복지몰 및 판촉몰, 멤버십몰 플랫폼에서 '보람라이프플랜' 상품을 판매한다.보람라이프플랜은 보람상조의 리빙 결합상품이다. 장례 서비스 혜택뿐 아니라 가전, 가구제품 등을 함께 소유할 수 있는 것이 특징이다. 만기 시 납입금 전액을 환급 받을 수 있다. 상조와 가전, 가구 제품이 필요한 소비자들에게 매력적인 상품으로 평가받는다.보람상조플러스가 비즈마켓, 이해라이프스타일과 3자 간 B2B 업무협약을 체결했다. ⓒ 보람그룹정종일 보람상조플러스 대표이사는 ""이번 업무협약은 상조업계 선도기업 보람상조와 B2B전문 서비스 전문기업 비즈마켓, 그리고 가구문화 혁신을 이루고 있는 이해라이프스타일이 만나 새로운 기회와 가치를 창출하는 것""이라며 ""궁극적으로 고객에게 더 많은 경험을 제공하고 만족을 주는 토털 라이프케어 서비스 기업의 역할을 다할 수 있도록 최선을 다하겠다""고 말했다.비즈마켓은 공공기관이나 민간기업을 대상으로 △임직원 복지몰 △판촉몰 △멤버십몰 등의 서비스를 제공하는 B2B 솔루션 전문 기업이다.신한금융그룹, KB금융그룹, 현대해상 등의 국내 유수의 기업이 비즈마켓을 통해 온라인몰을 이용하고 있다. 연간 거래액은 3000억원에 달한다. 이해라이프스타일은 가구 구독 서비스인 살구, 달달구독 등을 운영하는 기업이다.허탁 비즈마켓 대표는 ""3자 간 업무협약은 각 사의 B2B 영업 활성화를 위한 새로운 시도라고 할 수 있다""며 ""B2B플랫폼의 대표주자로서 다양한 산업군에서 이룬 성과처럼 이번 협약이 성공적인 사례로 남길 기대한다""고 전했다.이번 협약은 보람상조의 다양한 제휴 비즈니스에 활력을 불어넣을 것으로 전망된다. 최근 이미지 혁신과 사업 확장을 위해 사명을 변경한 보람상조플러스는 기존의 정체성을 넘어 고품격 상조서비스를 제공하겠다는 의지를 밝힌 바 있다."
sentence = "보람상조는 플랫폼 기업 비즈마켓과 협약을 맺어 상품을 판매한다. 보람상조의 리빙 결합상품인 '보람라이프플랜'이 상조와 가전 가구 제품이 필요한 소비자들에게 매력적으로 평가받는다. 이번 협약으로 보람상조의 다양한 제휴 비즈니스가 활성화될 것으로 전망된다."


# Universal Sentence Encoder를 로드합니다
model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# 문장이나 문서를 벡터로 변환합니다
document_embedding = model([document])
sentence_embedding = model([sentence])

# 문서와 문장 간의 코사인 유사도를 계산합니다
similarity_score = cosine_similarity(document_embedding, sentence_embedding)

print(f"score: {similarity_score[0][0]}")

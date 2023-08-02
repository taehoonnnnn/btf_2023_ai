import konlpy 
from konlpy.tag import Okt

# 요약문과 키워드 리스트
summary = "국내 은행 연체율이 4월말 기준 0.37%로 32개월만에 최고 수준을 기록했다. 기업대출과 가계대출의 연체율이 상승한 것이 원인이다. 금감원은 이러한 추세가 계속될 수 있으며 건전성 관리와 손실흡수능력을 강화할 것을 약속했다."
keywords = ["은행권 연체율", "금융감독원", "기업 연체율", "추세 유지", "가계대출 연체율"]

# 형태소 분석기 초기화
okt = Okt()

# 요약문을 형태소로 분리
summary_morphs = okt.morphs(summary)

# 키워드 점수 초기화
keyword_scores = {keyword: 0 for keyword in keywords}

# 각 형태소가 키워드에 포함되는지 확인하고, 포함되면 해당 키워드의 점수 증가
for morph in summary_morphs:
    for keyword in keywords:
        if morph in keyword:
            keyword_scores[keyword] += 1

# keyword_scores의 평균값 계산
average_score = sum(keyword_scores.values()) / len(keyword_scores)

print("평균 키워드 점수:", average_score)

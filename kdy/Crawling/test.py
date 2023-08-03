from konlpy.tag import Okt
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 다운로드 받은 폰트 파일의 경로를 설정합니다.
font_path = 'NanumGothic.ttf' 

# 폰트 파일을 matplotlib의 폰트로 설정합니다.
font_prop = fm.FontProperties(fname=font_path)

def textrank_keyword_visualization(text):
    # Konlpy의 Okt 형태소 분석기를 사용하여 문장을 토큰화합니다.
    okt = Okt()
    tokens = okt.phrases(text)

    # 토큰들을 그래프의 노드로 사용하고, 각 노드들을 연결합니다.
    graph = nx.Graph()
    graph.add_nodes_from(tokens)

    # 토큰들 사이에 엣지를 추가합니다. 이 예제에서는 각 토큰이 문장 내에서 인접한 경우에만 엣지를 추가합니다.
    for i in range(len(tokens) - 1):
        edge = (tokens[i], tokens[i+1])
        if not graph.has_edge(*edge):
            graph.add_edge(*edge)

    # 그래프를 시각화합니다.
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    for node, (x, y) in pos.items():
        plt.text(x, y, node, fontsize=10, ha='center', va='center', fontproperties=font_prop)
    plt.show()

text = """
은행권은 26일 제2차 은행권 금융시장 점검회의에서 은행채 발행을 최소화하겠다고 전했다. ⓒ 금융위원회[프라임경제] 금융위원회(금융위)는 금융감독원·5대(국민·신한·하나·우리·농협) 은행 부행장과 '제 2차 은행권 금융시장 점검회의'를 개최했다고 26일 밝혔다.금융위에 따르면 이 자리는 은행 통합 유동성커버리지비율(LCR) 정상화 조치를 6개월 유예하기로 결정한 지난 제1차 점검회의 영향을 살펴보기 위해 마련됐다.앞서 금융위는 코로나19 대응 과정에서 85%까지 완화했던 LCR 규제를 단계적으로 정상화하기로 결정했다. 이에 따라 은행들은 LCR 비율을 오는 12월까지 92.5%, 내년 1월부터 95%로 맞춰야했다.은행들은 유동성을 확보해 규제비율을 맞추고자 은행채 발행에 나섰고 이로 인해 금융채 금리상승(가격 하락)이 발생했다. 결국 LCR 비율 정상화가 채권시장 불안을 더욱 심화시키자 금융당국에서 정상화를 유예하기로 결정한 것이다.이번 회의에서 은행 관계자들은 LCR 정상화 유예로 자금 공급여력이...
"""

textrank_keyword_visualization(text)

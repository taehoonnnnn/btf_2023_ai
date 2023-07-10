import csv

# 결과를 저장할 리스트를 초기화합니다.
filtered_rows = []

# csv 파일을 열고 읽어옵니다.
with open('자본시장_금융_origin.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        # 만약 현재 행의 필드 개수가 5개라면 결과 리스트에 추가합니다.
        if len(row) == 5:
            filtered_rows.append(row)

# 필터링된 결과를 새로운 csv 파일에 저장합니다.
with open('자본시장_금융_clear_1.csv', 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(filtered_rows)

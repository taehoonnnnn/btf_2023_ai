import pandas as pd

# 원본 CSV 파일을 읽어옵니다.
source_file_path = 'crawl/부동산_기업.csv'
data = pd.read_csv(source_file_path)

# 원하는 열의 순서를 리스트로 지정합니다.
desired_column_indices = [0, 1, 2, 3, 4]  # 이 순서대로 가져올 열의 인덱스입니다.

# 선택한 열을 포함한 데이터프레임을 생성합니다.
selected_data = data.iloc[:, desired_column_indices]

# 새로운 CSV 파일로 저장합니다.
output_file_path = 'db.csv'
selected_data.to_csv(output_file_path, index=False)

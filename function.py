from pptx import Presentation
import pandas as pd

backgroud_image = "./data/background_img/img_no{n}"
initial_presentation = "./data/table_format.pptx"

prs = Presentation(initial_presentation)

def table_to_dataframe(slide):
    for shape in slide.shapes:
        if shape.has_table:
            table = shape.table
            # 테이블 데이터 읽기
            data = [[cell.text for cell in row.cells] for row in table.rows]
            # DataFrame 생성
            df = pd.DataFrame(data)
            return df
    return pd.DataFrame()  # 테이블이 없는 경우 빈 DataFrame 반환

# 첫 번째 슬라이드에서 DataFrame 생성
df = table_to_dataframe(prs.slides[0])

# DataFrame 출력
print(df)
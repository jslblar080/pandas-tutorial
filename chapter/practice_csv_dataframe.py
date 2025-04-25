import requests
import pandas as pd
from io import BytesIO

from base_chapter import BaseChapter


class PracticeCsvDataframe(BaseChapter):

    def __init__(self):
        super(PracticeCsvDataframe, self).__init__()
        print("CSV 입출력 연습\n")

    def play(self) -> None:
        url = "https://raw.githubusercontent.com/plotly/datasets/master/wellspublic.csv"
        response = requests.get(url)

        df = pd.read_csv(BytesIO(response.content))
        five_columns = df.columns[0:5]
        df = df[five_columns]

        df.to_csv("datasets/wellspublic_brief.csv", index=False)

        df = pd.read_csv("datasets/wellspublic_brief.csv")
        print(df.head())
        """
               API_WellNo  Cnty   Hole  SideTrck  Completion
        0  31000171670000     0  17167         0           0
        1  31000321820000     0  32182         0           0
        2  31000664470000     0  66447         0           0
        3  31001010720000     1   1072         0           0
        4  31001010730000     1   1073         0           0
        """

import requests
import pandas as pd
from io import BytesIO

from base_chapter import BaseChapter


class LearnCsvDataframe(BaseChapter):

    def __init__(self):
        super(LearnCsvDataframe, self).__init__()
        print("CSV 입출력 학습\n")

    def play(self) -> None:
        url = 'https://raw.githubusercontent.com/plotly/datasets/master/supermarket_Sales.csv'
        response = requests.get(url)

        df = pd.read_csv(BytesIO(response.content))

        df.to_csv("datasets/supermarket_Sales_index_false.csv", index=False)

        df = pd.read_csv("datasets/supermarket_Sales_index_false.csv")
        print(df.head())
        """
            Invoice ID Branch  ... Gross income Customer stratification rating
        0  750-67-8428      A  ...      26.1415                            9.1
        1  226-31-3081      C  ...       3.8200                            9.6
        2  631-41-3108      A  ...      16.2155                            7.4
        3  123-19-1176      A  ...      23.2880                            8.4
        4  373-73-7910      A  ...      30.2085                            5.3

        [5 rows x 17 columns]
        """

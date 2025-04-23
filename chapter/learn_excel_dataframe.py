import requests
import pandas as pd
from io import BytesIO

from base_chapter import BaseChapter


class LearnExcelDataframe(BaseChapter):

    def __init__(self):
        super(LearnExcelDataframe, self).__init__()
        print("액셀 입출력 학습\n")

    def play(self) -> None:
        url = 'https://raw.githubusercontent.com/plotly/datasets/master/supermarket_sales.xlsx'
        response = requests.get(url)

        df = pd.read_excel(BytesIO(response.content), sheet_name="January")
        print(df.head())
        """
            Invoice ID Branch       City  ...    cogs gross income Rating
        0  316-68-6352      A     Yangon  ...   72.72       3.6360    7.1
        1  522-57-8364      A     Yangon  ...  410.72      20.5360    7.6
        2  679-22-6530      B   Mandalay  ...   81.24       4.0620    4.1
        3  606-80-4905      C  Naypyitaw  ...  114.90       5.7450    6.8
        4  426-39-2418      C  Naypyitaw  ...  429.87      21.4935    9.8

        [5 rows x 16 columns]
        """
        df = pd.read_excel(BytesIO(response.content), sheet_name="February")
        print(df.head())
        """
            Invoice ID Branch       City  ... gross margin percentage gross income Rating
        0  130-98-8941      C  Naypyitaw  ...                4.761905      22.4910    5.7
        1  326-71-2155      C  Naypyitaw  ...                4.761905      14.7900    6.1
        2  746-19-0921      C  Naypyitaw  ...                4.761905       1.0790    7.2
        3  870-76-1733      A     Yangon  ...                4.761905       3.5575    4.4
        4  453-33-6436      A     Yangon  ...                4.761905      37.2480    6.8

        [5 rows x 17 columns]
        """
        dict = pd.read_excel(BytesIO(response.content), sheet_name=None)
        print(dict.keys())
        """
        dict_keys(['January', 'February', 'March'])
        """
        print(dict["March"].head())
        """
            Invoice ID Branch      City  ... gross margin percentage gross income Rating
        0  276-75-6884      A    Yangon  ...                4.761905      10.3065    8.7
        1  701-69-8742      B  Mandalay  ...                4.761905      17.1850    6.7
        2  595-11-5460      A    Yangon  ...                4.761905       9.6580    5.1
        3  856-22-8149      A    Yangon  ...                4.761905       1.2645    6.1
        4  865-92-6136      A    Yangon  ...                4.761905       7.9125    9.3

        [5 rows x 17 columns]
        """

        dict["January"].to_excel("datasets/supermarket_sales_index_true.xlsx", index=True)

        dict2 = pd.read_excel("datasets/supermarket_sales_index_true.xlsx", sheet_name=None)
        print(dict2["Sheet1"].head())
        """
           Unnamed: 0   Invoice ID Branch  ...    cogs gross income Rating
        0           0  316-68-6352      A  ...   72.72       3.6360    7.1
        1           1  522-57-8364      A  ...  410.72      20.5360    7.6
        2           2  679-22-6530      B  ...   81.24       4.0620    4.1
        3           3  606-80-4905      C  ...  114.90       5.7450    6.8
        4           4  426-39-2418      C  ...  429.87      21.4935    9.8

        [5 rows x 17 columns]
        """

        dict["January"].to_excel("datasets/supermarket_sales_index_false.xlsx", sheet_name="January", index=False)

        dict2 = pd.read_excel("datasets/supermarket_sales_index_false.xlsx", sheet_name=None)
        print(dict2["January"].head())
        """
            Invoice ID Branch       City  ...    cogs gross income Rating
        0  316-68-6352      A     Yangon  ...   72.72       3.6360    7.1
        1  522-57-8364      A     Yangon  ...  410.72      20.5360    7.6
        2  679-22-6530      B   Mandalay  ...   81.24       4.0620    4.1
        3  606-80-4905      C  Naypyitaw  ...  114.90       5.7450    6.8
        4  426-39-2418      C  Naypyitaw  ...  429.87      21.4935    9.8

        [5 rows x 16 columns]
        """

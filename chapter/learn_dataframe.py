import pandas as pd

from base_chapter import BaseChapter
from util.print import Print


class LearnDataFrame(BaseChapter):

    def __init__(self):
        super(LearnDataFrame, self).__init__()
        print("데이터프레임 학습\n")

    def play(self) -> None:
        df = pd.DataFrame([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], columns=['가', '나', '다'])
        Print.data_with_type(df)

        dict_data = {
            "name": ["Kim", "Lee", "Park"],
            "age": [24, 27, 34],
            "children": [2, 1, 3]
        }
        df = pd.DataFrame(dict_data)
        Print.data_with_type(df)
        print(df.index)  # RangeIndex(start=0, stop=3, step=1)
        print(df.columns)  # Index(['name', 'age', 'children'], dtype='object')
        print(df.dtypes)
        """
        name        object
        age          int64
        children     int64
        dtype: object
        """
        df.index = list("abc")
        print(df.T, '\n')
        """
                    a    b     c
        name      Kim  Lee  Park
        age        24   27    34
        children    2    1     3
        """
        Print.data_with_type(df["name"])
        """
        Data:
        a     Kim
        b     Lee
        c    Park
        Name: name, dtype: object
        Type:
        <class 'pandas.core.series.Series'>
        """
        Print.data_with_type(df[["name", "children"]])  # fancy indexing
        """
        Data:
           name  children
        a   Kim         2
        b   Lee         1
        c  Park         3
        Type:
        <class 'pandas.core.frame.DataFrame'>
        """
        df.rename(columns={"name": "이름"})
        print(df)
        """
           name  age  children
        a   Kim   24         2
        b   Lee   27         1
        c  Park   34         3
        """
        df.rename(columns={"name": "이름"}, inplace=True)
        print(df)
        """
             이름  age  children
        a   Kim   24         2
        b   Lee   27         1
        c  Park   34         3
        """

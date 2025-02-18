import pandas as pd

from base_chapter import BaseChapter


class PracticeDataFrame(BaseChapter):

    def __init__(self):
        super(PracticeDataFrame, self).__init__()
        print("데이터프레임 연습\n")

    def play(self) -> None:
        df = pd.DataFrame([
            ["KFC", 1000, 4.5],
            ["McDonald", 2000, 3.9],
            ["SchoolFood", 2500, 4.2]
        ], columns=["food", "price", "rating"])
        print(df, '\n')
        """
        	food	price	rating
        0	KFC	        1000	4.5
        1	McDonald	2000	3.9
        2	SchoolFood	2500	4.2
        """

        print(df[["food", "rating"]], '\n')
        """
                 food  rating
        0         KFC     4.5
        1    McDonald     3.9
        2  SchoolFood     4.2
        """

        df.rename(columns={"food": "place"}, inplace=True)
        print(df)
        """
                place  price  rating
        0         KFC   1000     4.5
        1    McDonald   2000     3.9
        2  SchoolFood   2500     4.2
        """

import pandas as pd
import numpy as np

from base_chapter import BaseChapter


class PracticeSeries(BaseChapter):

    def __init__(self):
        super(PracticeSeries, self).__init__()
        print("시리즈 연습\n")

    def play(self) -> None:
        print(pd.Series(np.arange(3, 12, 2), dtype="float32"), '\n')
        """
        0     3.0
        1     5.0
        2     7.0
        3     9.0
        4    11.0
        dtype: float32
        """

        print(pd.Series(list("가나다라마")), '\n')
        """
        0    가
        1    나
        2    다
        3    라
        4    마
        dtype: object
        """

        sample = pd.Series(np.arange(10, 60, 10), index=list("가나다라마"))

        print(sample, '\n')
        """
        가    10
        나    20
        다    30
        라    40
        마    50
        dtype: int64
        """

        print(sample[['나', '라']], '\n')
        """
        나    20
        라    40
        dtype: int64
        """

        np.random.seed(20)
        sample2 = pd.Series(np.random.randint(100, 200, size=15), dtype="int64")

        print(sample2[sample2 <= 160], '\n')
        """
        2     115
        4     128
        6     109
        7     120
        9     122
        11    134
        13    140
        dtype: int64
        """

        print(sample2[(sample2 >= 130) & (sample2 <= 170)], '\n')
        """
        11    134
        13    140
        dtype: int64
        """

        print(pd.Series(["apple", np.nan, "banana", "kiwi", "gubong"], index=list("가나다라마")), '\n')
        """
        가     apple
        나       NaN
        다    banana
        라      kiwi
        마    gubong
        dtype: object
        """

        sample = pd.Series(["IT서비스", np.nan, "반도체", np.nan, "바이오", "자율주행"])

        print(sample[sample.isna()], '\n')
        """
        1    NaN
        3    NaN
        dtype: object
        """

        print(sample[sample.notna()], '\n')
        """
        0    IT서비스
        2      반도체
        4      바이오
        5     자율주행
        dtype: object
        """

        np.random.seed(0)
        sample = pd.Series(np.random.randint(100, 200, 10), dtype="int64")

        print(sample[2:7], '\n')
        """
        2    164
        3    167
        4    167
        5    109
        6    183
        dtype: int64        
        """

        np.random.seed(0)
        sample2 = pd.Series(
            np.random.randint(100, 200, 10),
            index=list("가나다라마바사아자차"),
            dtype="int64"
        )

        print(sample2['바':'차'], '\n')
        """
        바    109
        사    183
        아    121
        자    136
        차    187
        dtype: int64
        """

        print(sample2['가':'다'], '\n')
        """
        가    144
        나    147
        다    164
        dtype: int64
        """

        print(sample2['나':'바'])
        """
        나    147
        다    164
        라    167
        마    167
        바    109
        dtype: int64
        """

import pandas as pd
import numpy as np
from base_chapter import BaseChapter
from util.print import Print


class LearnSeries(BaseChapter):

    def __init__(self):
        print("Pandas version:", pd.__version__, '\n')

        ndarray = np.arange(100, 105)
        series = pd.Series(ndarray)  # dtype: int64
        Print.data_with_type(series)
        series = pd.Series(ndarray, dtype="int32")
        Print.data_with_type(series)

        list_data = ["부장", "차장", "대리", "사원", "인턴"]
        series = pd.Series(list_data)  # dtype: object
        Print.data_with_type(series[1:4])  # slicing
        series.index = list("abcde")
        Print.data_with_type(series['b':'d'])  # slicing
        Print.data_with_type(series.values)  # ['부장' '차장' '대리' '사원' '인턴'] <class 'numpy.ndarray'>

        list_data = [91, 2.5, "스포츠", 4, 5.16]
        series = pd.Series(list_data)  # dtype: object
        Print.data_with_type(series)
        print(series.index)  # RangeIndex(start=0, stop=5, step=1)
        print(series[2])  # 스포츠
        print(series[[0, 3]])  # fancy indexing
        print(series[np.arange(0, 5, 3)], '\n')  # fancy indexing
        series = pd.Series(list_data, index=['a', 'b', 'c', 'd', 'e'])
        Print.data_with_type(series)
        print(series.index)  # Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
        print(series['c'])  # 스포츠
        print(series[['a', 'd']], '\n')  # fancy indexing

        np.random.seed(0)
        ndarray = np.random.randint(10000, 20000, size=10)
        series = pd.Series(ndarray > 15000)  # dtype: bool
        Print.data_with_type(series)
        filtered_series = pd.Series(ndarray, dtype="int64")[series]  # boolean indexing
        Print.data_with_type(filtered_series)
        print(filtered_series.ndim)  # 1
        Print.data_with_type(filtered_series.shape)  # (5,) <class 'tuple'>

        list_data = ["선화", "강호", np.nan, "소정", "우영"]  # nan: not a number
        series = pd.Series(list_data)
        Print.data_with_type(series)
        Print.data_with_type(series.isnull())  # dtype: bool
        Print.data_with_type(series.isna())  # dtype: bool
        Print.data_with_type(series.notnull())  # dtype: bool
        Print.data_with_type(series.notna())  # dtype: bool
        filtered_series = series[series.notna()]  # boolean indexing
        Print.data_with_type(filtered_series)

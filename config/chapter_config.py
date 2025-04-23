from base_chapter import BaseChapter
from chapter.learn_csv_dataframe import LearnCsvDataframe
from chapter.learn_dataframe import LearnDataFrame
from chapter.learn_excel_dataframe import LearnExcelDataframe
from chapter.learn_series import LearnSeries
from chapter.practice_dataframe import PracticeDataFrame
from chapter.practice_series import PracticeSeries


class ChapterConfig:

    @staticmethod
    def chapter() -> BaseChapter:
        return LearnCsvDataframe()

from base_chapter import BaseChapter
from chapter.learn_series import LearnSeries
from chapter.practice_series import PracticeSeries


class ChapterConfig:

    @staticmethod
    def chapter() -> BaseChapter:
        return PracticeSeries()

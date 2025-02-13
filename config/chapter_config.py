from base_chapter import BaseChapter
from chapter.learn_series import LearnSeries


class ChapterConfig:

    def __init__(self):
        self.learn_series()

    @staticmethod
    def learn_series() -> BaseChapter:
        return LearnSeries()

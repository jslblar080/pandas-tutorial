from base_chapter import BaseChapter
from chapter.learn_series import LearnSeries


class ChapterConfig:

    def __init__(self):
        self.chapter()

    @staticmethod
    def chapter() -> BaseChapter:
        return LearnSeries()

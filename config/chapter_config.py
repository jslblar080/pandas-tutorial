from base_chapter import BaseChapter
from chapter.learn_series import LearnSeries


class ChapterConfig:

    @staticmethod
    def chapter() -> BaseChapter:
        return LearnSeries()

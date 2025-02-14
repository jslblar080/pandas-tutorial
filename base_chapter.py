from abc import ABC, abstractmethod


class BaseChapter(ABC):

    @abstractmethod
    def play(self) -> None:
        pass

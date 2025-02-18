from abc import ABC, abstractmethod


class BaseChapter(ABC):

    def __init__(self):
        print("챕터: ", end="")

    @abstractmethod
    def play(self) -> None:
        pass

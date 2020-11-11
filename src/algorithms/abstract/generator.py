from abc import abstractmethod, ABC

class ClipGenerator(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def generate(self):
        raise NotImplementedError

    @abstractmethod
    def info(self) -> str:
        raise NotImplementedError

from abc import ABC , abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
com=Computer()
com.process()

import abc
from abc import ABC ,abstractmethod
class R(ABC):
    @abstractmethod
    def rk(self):
        print("abstract base classes")
class K(R):
    def rk(self):
        super().rk()
        print("subclass")
r=K()
r.rk()

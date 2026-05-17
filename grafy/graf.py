from abc import ABC, abstractmethod

class Graph(ABC):

    @abstractmethod
    def neighbors(self, v):
        pass

    @abstractmethod
    def add_edge(self, u, v):
        pass

    @abstractmethod
    def has_edge(self, u, v):
        pass

    @abstractmethod
    def vertices(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
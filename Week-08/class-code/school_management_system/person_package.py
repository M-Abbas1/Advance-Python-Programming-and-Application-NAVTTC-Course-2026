from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, n, a, e):
        self.name = n
        self.age = a
        self.email = e

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def get_summary(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
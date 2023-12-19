import abc
from abc import ABC, abstractmethod


class Bird(ABC):
    def __init__(self,eat):
        self.eat = eat

    @abstractmethod
    def fly(self):
        ...

    @abstractmethod
    def living(self):
        ...

    @abstractmethod
    def feet(self):
        ...

    @abstractmethod
    def color(self):
        ...


class Eagle(Bird):
    def __init__(self, eat):
        super().__init__(eat)

    def fly(self):
        return 'I can fly'

    def living(self):
        return "I'm living in trees"

    def feet(self):
        return "I have talons adapted for catching and holding prey"

    def color(self):
        return " I  have white heads and tails with dark brown bodies and wings"


class Penguin(Bird):
    def __init__(self,eat):
        super().__init__(eat)

    def fly(self):
        return "I can't fly"

    def living(self):
        return "I'm living in Antarctica"

    def feet(self):
        return "I have feet suitable for walking"

    def color(self):
        return " I have dark on the dorsal (back) surface and white on the ventral (underside) surface"


eagle1 = Eagle('mis')
penguin1 = Penguin('dzuk')
print(eagle1.fly(), eagle1.feet(),  end ='\t')

print(Penguin.mro())


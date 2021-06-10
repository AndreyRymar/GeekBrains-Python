# homework_lesson_7_task2
"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
    — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
    V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
    для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
    реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, cloth):
        self.cloth = cloth

    @abstractmethod
    def flow(self):
        pass

class Coat(Clothes):
    def __init__(self, cloth):
        super().__init__(cloth)

    @property
    def flow(self):
        return self.cloth / 6.5 + 0.5

class Costume(Clothes):
    def __init__(self, cloth):
        super().__init__(cloth)

    @property
    def flow(self):
        return self.cloth * 2 + 0.3

my_coat = Coat(6)
print(my_coat.flow)

my_costume = Costume(13)
print(my_costume.flow)

print(f'Общий расход ткани: {my_coat.flow + my_costume.flow}')
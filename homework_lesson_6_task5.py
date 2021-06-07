# homework_lesson_6_task5
"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить
    уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки для класса Pen.')

class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки для класса Pencil.')

class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки для класса Handle.')

my_Stationery = Stationery('')
my_Stationery.draw()

my_Pen = Pen('Pen')
my_Pen.draw()

my_Pencil = Pencil('Pencil')
my_Pencil.draw()

my_Handle = Handle('Handle')
my_Handle.draw()

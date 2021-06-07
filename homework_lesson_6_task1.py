# homework_lesson_6_task1
"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
 зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
 третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
 порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
 завершать скрипт.
"""
from time import sleep

class TrafficLight:
    my_dict_color = ["Красный", "Желтый", "Зеленый"]

    def __init__(self, color):
        self.__color = color

    def running(self):
        for my_color in self.my_dict_color:
            print(f'Цвет {my_color}')
            if my_color == "Красный":
                sleep(7)
                self.__color = self.my_dict_color.index(my_color)+1
            elif my_color == "Желтый":
                sleep(2)
                self.__color = self.my_dict_color.index(my_color)+1
            else:
                sleep(1)
                self.__color = self.my_dict_color.index(my_color)+1


a = TrafficLight("Красный")
a.running()
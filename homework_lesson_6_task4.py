# homework_lesson_6_task4
"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
    is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
   который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = {True, False}

    def go(self):
        print(f'Машина поехада')

    def stop(self):
        print(f'Машина остановилась')

    def turn(self):
        print(f'Машина повернула')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')
        if self.speed > 60:
            print(f'Внимание. Скорость более 60 !')

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')
        if self.speed > 60:
            print(f'Внимание. Скорость более 60 !')

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
my_Car = Car(78, 'Оранжевая', 'Митсубиши', False)
my_Car.go()
my_Car.turn()
my_Car.stop()
my_Car.show_speed()

my_TownCar = TownCar(78, 'Оранжевая', 'Митсубиши', False)
my_TownCar.go()
my_TownCar.turn()
my_TownCar.stop()
my_TownCar.show_speed()


my_PoliceCar = PoliceCar(70, 'Красная', 'Ламборгини', True)
my_PoliceCar.go()
my_PoliceCar.turn()
my_PoliceCar.stop()
my_PoliceCar.show_speed()



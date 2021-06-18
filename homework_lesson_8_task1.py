# homework_lesson_8_task1
"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_to_int(cls, date_fabric):
        my_date = []

        for i in date_fabric.replace('-',' ').split():
            my_date.append(i)

        return f'Дата в формате чисел: день {int(my_date[0])}, месяц {int(my_date[1])}, год {int(my_date[2])}'

    @staticmethod
    def valid(date_static):
        try:
            day, month, year = date_static.split()
            if int(day) not in range(1, 32):
                raise ValueError("Вы ввели день вне диапазона календаря!")
            if int(month) not in range(1, 13):
                raise ValueError("Вы ввели месяц вне диапазона календаря!")
            if int(year) not in range(1, 2022):
                raise ValueError("Вы ввели год вне диапазона календаря!")
        except ValueError as err:
            print(err)
        else:
            print('Валидация даты прошла успешно')


my_date_1 = Data('16-06 2021')
print(Data.get_to_int('16-06 2021'))
print(Data.get_to_int('11-06-2021'))
print()

Data.valid('13 09 2002')
Data.valid('41 09 2002')
Data.valid('11 15 2002')

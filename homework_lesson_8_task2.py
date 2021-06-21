# homework_lesson_8_task2
"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
    завершиться с ошибкой.
"""
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def delenie(value_1, value_2):
    try:
        value_1 = int(value_1)
        value_2 = int(value_2)
        if value_2 == 0:
            raise OwnError('Деление на ноль невозможно')
    except ValueError:
        print("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        print(f'Все хорошо. Результат вычисления:  {value_1/value_2}')


delenie(6, 'dfgfdg')
print()
delenie(6, 0)
print()
delenie(6, 2)
print()

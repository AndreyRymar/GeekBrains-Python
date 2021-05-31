# homework_lesson_4_task6
"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle
j = 3
my_list = [1, 11, 21, 31, 41, 51]
my_count = 0

for i in count(j):
    if i > j+7:
        break
    print(i)

for i in cycle(my_list):
    if i == my_list[0]:
        my_count += 1
    if my_count < 5:
        print(i)
    else:
        break
# homework_lesson_4_task5
"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
import functools

my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(my_list)

def my_func(j, i):
    return j*i

value = functools.reduce(my_func, my_list)
print(value)
# homework_lesson_8_task7
"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.

Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата.
"""
class ComplexNumber:

    def __init__(self, rez, imz):
        self.rez = rez
        self.imz = imz

    def __add__(self, other):
        return ComplexNumber(self.rez + other.rez, self.imz + other.imz)

    def __mul__(self, other):
        return ComplexNumber(self.rez * other.rez - self.imz * other.imz, self.imz * other.rez + self.rez * other.imz)

    def __str__(self):
        return f'{self.rez} + {self.imz}i'

my_comp_1 = ComplexNumber(6, 2)
my_comp_2 = ComplexNumber(-3, 2)
print(f'Сумма : {my_comp_1 + my_comp_2}')
print(f'Произведение : {my_comp_1 * my_comp_2}')

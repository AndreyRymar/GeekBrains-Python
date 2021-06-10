# homework_lesson_7_task1
"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
    который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
    (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
    с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        my_str = 'Матрица: \n'
        for i in self.my_matrix:
            for j in i:
                my_str += str(f'{j}\t')
            my_str +='\n'
        return my_str

#Мой вариант:
    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.my_matrix)):
            temp_row = []
            for j in range(len(self.my_matrix[i])):
                temp_row.append(self.my_matrix[i][j] + other.my_matrix[i][j])
            new_matrix.append(temp_row)
        return Matrix(new_matrix)

my_matrix1 = Matrix([[1, 2, 6, 8], [1, 2, 5, 7], [3, 4, 7, 8]])
print(my_matrix1)

my_matrix2 = Matrix([[80, 10, 60, 80], [70, 50, 20, 10], [80, 30, 70, 30]])
print(my_matrix2)
print(f'Новая суммарная матрица: {my_matrix1 + my_matrix2}')

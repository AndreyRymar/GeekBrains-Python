"""
 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
"""
# a = 2
# b = "Andrew"
# print(a)
# a += a
# print(a)
# print(b)

# name = input("Ведите Ваше имя: ")
# age = int(input("Введите Ваш возвраст: "))
# print(f"Здравствуй, {name}! Твой возраст {age}")

"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.
"""

# time = int(input("Введите время в секундах "))
# hour = time // 3600
# time = time % 3600
# minutes = time // 60
# seconds = time % 60
# print(f"Введенное значение {hour} часов :{minutes} минут :{seconds} секунд")

"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. 
Считаем 3 + 33 + 333 = 369.
"""
# n = int(input("Введите число: "))
# total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
# print(f"Сумма чисел 'n + nn + nnn' равна {total} ")

"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл 
while и арифметические операции.
"""
# n = int(input("Введите целое положительное число: "))
# max = n % 10
# while n >= 1:
#     n = n // 10
#     if n % 10 > max:
#         max = n % 10
#     if n > 9:
#         continue
#     else:
#         print("Максимальное цифра в числе ", max)
#         break

"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
 фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. 
 Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите 
 численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
# proceeds = float(input("Введите выручку фирмы "))
# costs = float(input("Введите издержки фирмы "))
# if proceeds > costs:
#     print(f"Фирма работает с прибылью. Рентабельность выручки составила {proceeds / costs:.2f}")
#     staff = int(input("Введите количество сотрудников фирмы "))
#     print(f"прибыль в расчете на одного сторудника сотавила {proceeds / staff:.2f}")
# elif proceeds == costs:
#     print("Фирма работает в ноль")
# else:
#     print("Фирма работает в убыток")

"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
 спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
  результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить
   одно натуральное число — номер дня.
"""
# a = int(input("Введите результат пробежки первого дня в км "))
# b = int(input("Введите общий желаемый результат в км "))
# days = 1
# while a < b:
#         a = a + 0.1 * a
# #       print(a)
#         days += 1
# print(f"Номер дня, на котором достигнут результат {days}")

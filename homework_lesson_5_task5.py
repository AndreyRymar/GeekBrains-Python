# homework_lesson_5_task5
"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('task_5.txt', 'w', encoding='utf-8') as fw:
    my_input = input('Введите набор чисел, разделенных пробелом : ')
    fw.write(my_input)

count = 0

with open('task_5.txt', encoding='utf-8') as f:
    line = f.read()
    for i in line.split():
        count +=int(i)
print(count)

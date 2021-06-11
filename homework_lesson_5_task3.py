# homework_lesson_5_task3
"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
value = 0
my_count = 0

with open('task_3.txt', encoding='utf-8') as f:
    my_list = f.readlines()
    for i in my_list:
        j, k = i.split()
        value += int(k)
        my_count += 1
        if int(k) < 20000:
            print('Оклад менее 20т.р. у содрудника:', j)
    my_avarage = value / my_count
    print(f'Средний доход: {my_avarage}')


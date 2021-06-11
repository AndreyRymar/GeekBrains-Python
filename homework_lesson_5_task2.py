# homework_lesson_5_task2
"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
with open('task_2.txt', encoding='utf-8') as f:
    my_list = f.readlines()
    # print(my_list)
    print('Количество строк: ', len(my_list))
    for i in my_list:
        print(f'Колчество слов в строке "{i}": ', len(i.split()))

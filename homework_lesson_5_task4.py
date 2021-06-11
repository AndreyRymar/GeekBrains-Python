# homework_lesson_5_task4
"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый
файл.
"""
dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('task_4.txt', encoding='utf-8') as f:
    my_list = f.readlines()
    # print(my_list)
    for i in my_list:
        j, k = i.split(' — ')
        with open('task_4_2.txt', 'a', encoding='utf-8') as fw:
            fw.write(f'{dict[j]} - {k}')

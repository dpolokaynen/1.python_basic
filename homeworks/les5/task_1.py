'''
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

with open("task_1.txt", 'w') as new_file:
    while True:
        data = input()
        print(data, file=new_file)
        if input() == '':
            break

'''
Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

new_file = open("task_2.txt", "r", encoding='UTF-8')
content = new_file.readlines()
print(content)
string_number = len(content)
print (f'Количество строк в файле равно {string_number}')
counter = 0
while counter < string_number:
    word_number = len(content[counter].split())
    print(f'Количество строк в {counter} строке равно {word_number}')
    counter += 1
new_file.close()

'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
 построчно данные. При этом английские числительные должны заменяться на
 русские. Новый блок строк должен записываться в новый текстовый файл.
'''
translate_dictionary = {'one': 'один', 'two': 'два','three': 'три',
                        'four': 'четыре','five': 'пять','six': 'шесть','seven': 'семь',
                        'eight': 'восемь', 'nine': 'девять','ten': 'десять'}
new_file = open('task_4.txt', 'r')
result_file = open('task_4_result_file.txt', 'w')
for line in new_file:
    split_line = line.split(' - ')
    new_word = translate_dictionary.get(str.lower(split_line[0]))
    new_string = [new_word, split_line[1]]
    new_string = ' - '.join(new_string)
    result_file.write(new_string)
result_file.close()
new_file.close()

'''
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''

print('Введите строку из нескольких слов, разделенных пробелами')
input_string = input()
split_string = input_string.split()
words_number = len(split_string)
i = 0 # счетчик для цикла
while i <= words_number:
    if 0 < len(split_string[i]) <= 10:
        print(i + 1, split_string[i])
        i += 1
    else:
        print(i + 1, split_string[i][:10])
        i += 1
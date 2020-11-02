'''
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
 разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
 Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
 Необходимо использовать написанную ранее функцию int_func().
'''
def int_func(input_word):
    letters = list(input_word)
    capital_letter = letters[0].upper()
    other_words = ''.join(letters[1:])
    result_word =[capital_letter,other_words]
    capital_word = ''.join(result_word)
    return capital_word
    #print(f'{capital_letter}{other_words[1:]}')
print('Исходное слово - hello. После преобразования - ',int_func('hello'))
def capital_string(input_string):
    words = input_string.split(' ')
    counter = 0
    result_string = []
    while counter < len(words):
        result_string +=int_func(words[counter]) + ' '
        counter+=1
    result_string = ''.join(result_string)
    return result_string


print('Исходная строка - hello dear world. После преобразования - ',
      capital_string('Hello dear world'))
'''
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
символ, выполнение программы завершается. Если специальный символ введен после нескольких
чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
завершить программу.
'''
def my_range (start,stop,step):
    my_range_list = []
    while start <= stop:
        my_range_list.append(start)
        return my_range_list
        start += step
q = 1
sum = 0
while q:
    print('Введите числа, разделенные пробелом')
    input_number_list = input()
    input_numbers = input_number_list.split(' ')
    print(input_numbers)
    for number in input_numbers:
        try:
            sum +=float(number)
        except ValueError:
            break
    print(sum)
    print('Хотите ввести еще числа? да/нет')
    repeat = input()
    if repeat == 'да':
        q = 1
    elif repeat == 'нет':
        print('Итоговая сумма равна', sum)
        q = 0
    else:
        print('Введенно что-то другое')
        print('Итоговая сумма равна', sum)
        break
'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют
элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться
после них.
'''

'Введем список чисел'
my_list = [1, 4, 6, 8, 12, 453, 11, 0]
my_list.sort(reverse=True)
print(my_list)
q = 1 # переменная для выхода из цикла
while q == 1:
    print('Введите число')
    input_number = int(input())
    my_list.append(input_number)
    my_list.sort(reverse=True)
    print(my_list)
    print('Ввести еще одно число? (да/нет)')
    input_answer = input()
    if input_answer == 'да':
        q = 1
        my_list.append(input_number)
    else:
        break
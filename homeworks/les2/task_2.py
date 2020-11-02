'''
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''
q = 1 # переменная для выхода из цикла
input_list = []
while q == 1:
    print('Введите число')
    input_number = int(input())
    print('Ввести еще одно число? (да/нет)')
    input_answer = input()
    if input_answer == 'да':
        q = 1
        input_list.append(input_number)
    else:
        input_list.append(input_number)
        break
print(input_list)
changed_list = []
if len(input_list) % 2 == 0:
    i = 0 # счетчк для цикла
    while i < len(input_list):
        changed_list.append(input_list[i+1])
        changed_list.append(input_list[i])
        i = i + 2
else:
    i = 0
    while i < len(input_list)-1:
        changed_list.append(input_list[i + 1])
        changed_list.append(input_list[i])
        i = i + 2
    changed_list.append(input_list[-1])
print(changed_list)
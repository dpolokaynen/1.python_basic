'''
Создайте собственный класс-исключение, который должен проверять содержимое списка
на наличие только чисел. Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента
и вносить его в список, только если введено число. Класс-исключение должен не позволить
пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
'''

# class Is_number (Exception):
#     @staticmethod
#     def division(list_number):
#         try:
#             try:
#                 return dividend / divisor
#             except ZeroDivisionError:
#                 raise My_ZeroDivisionError()
#         except My_ZeroDivisionError:
#             return f'На ноль делить нельзя'
# print(My_ZeroDivisionError.division(2,0))

class Is_Digit(Exception):
    pass
list_number = list()
while True:
    element = input("Введите значение >>> ")

    if element == "quit":
        print(list_number)
        break

    try:
        if element.isdigit():
            list_number.append(float(element))
        else:
            raise Is_Digit
    except Is_Digit:
        print("Введенный элемент не явялется числом")

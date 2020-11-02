'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def division (number_1, number_2):
    try:
        result = number_1 / number_2
        print(result)
        return result
    except ZeroDivisionError:
        print('На ноль делить нельзя!')

print('Введите делимое число')
dividend = float(input())
print('Введите делитель число')
divider = float(input())
quotient = division(dividend, divider)
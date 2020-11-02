'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''
from functools import reduce
even_list = [number for number in range(100,1001) if number%2 ==0]
product = 1
for number in even_list:
    product *=number
print('Произведение чисел списка =',product)
'''
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.
'''

print('Решение через *')
def exponentiation_1 (positive_base, negative_degree):
    result_1 = positive_base**negative_degree
    print(result_1)
check_1 = exponentiation_1(15,-7)
print('Решение через цикл')

def exponentiation_2 (positive_base, negative_degree):
    counter = 0
    result_2 = 1
    factor = (1 /positive_base)
    while counter > negative_degree:
        result_2 *= (factor)
        counter -= 1
    print(result_2)


check_2 = exponentiation_2(15,-7)

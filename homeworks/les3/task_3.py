'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''
def min_number(a,b,c):
    list_number = (float(a), float(b), float(c))
    minimum = a+b+c
    for item in list_number:
        if minimum > item:
            minimum = item
    return minimum

def my_func(number_1, number_2, number_3):
   number_list = {float(number_1), float(number_2), float(number_3)}
   sum_max = number_1 + number_2 + number_3 - min_number(number_1,number_2,number_3)
   print('Сумма наибольших двух чисел из трех равна', sum_max)

result = my_func(1,2,-1)

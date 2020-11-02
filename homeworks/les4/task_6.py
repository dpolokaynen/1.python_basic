'''
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при
достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть
условие, при котором повторение элементов списка будет прекращено.
'''
from itertools import count,cycle
print('а)')
counter = 0
start = 1
for counter in cycle(count(start,1)):
     if counter <= 15:
         print(counter)
     else:
         break
print('b)')
print('Условие для выхода из цикла - 10 раз повторений')
initial_list = [1,2,4,6,'hello','shalom',2]
counter = 0
repeat = 0
start = 1
for counter in cycle(initial_list):
    if repeat <= 10*len(initial_list):
         print(counter)
         repeat += 1

    else:
         break
'''
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран.
'''

task_5 = open('task_5.txt', 'w')
print('Введите числа через пробел')
numbers_list = input()
numbers = numbers_list.split()
sum = 0
for number in numbers:
    sum +=int(number)
print(sum)
task_5.close()

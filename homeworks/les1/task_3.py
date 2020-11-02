'''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''
print('Введите число')
number = int(input())
number_sum = number + (10*number + number) + (100*number + 10*number + number)
print(number_sum)
'''
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
'''

print('Введите целое положительное число')
number = int(input())
digit_array = []
while number > 1/10:
    number_digit = number % 10
    number = number // 10
    digit_array.append(number_digit)
print(max(digit_array))
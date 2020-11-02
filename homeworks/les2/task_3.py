'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

month_list = ['зима', 'весна', 'лето', 'осень']
print('Введите номер месяца от 1 до 12')
month_number = int(input())
print('С помощью списка')
if month_number <= 2 or month_number > 11:
    print(month_list[0])
elif 3 <= month_number <= 5:
    print(month_list[1])
elif 6 <= month_number <= 8:
    print(month_list[2])
else:
    print(month_list[3])
print('С помощью словаря')
month_dictionary = {1:'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето',
                    7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень',
                    11: 'осень', 12: 'зима'}
print(month_dictionary[month_number])
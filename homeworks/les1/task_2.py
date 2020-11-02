'''
 Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
'''

print('Введите время в секундах')
time_seconds = input()
hours = int(time_seconds) // 3600
minutes = int(time_seconds) // 60 - hours * 60
seconds = int(time_seconds) % 60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
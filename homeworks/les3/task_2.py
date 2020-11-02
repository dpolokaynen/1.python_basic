'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
'''

def welcome(name, surname, birth_year, city, email, phone_number):
    print(f'Пользователь {name} {surname}, {birth_year} года рождения, проживает в {city}, '
          f'email: {email} контактный телефон: {phone_number}')

user_info = welcome(name = 'Daniil', surname = 'Polokaynen', birth_year = 1996, city = 'Moscow',
                email = 'poldaniel@list.ru', phone_number = '8-985-478-23-62')
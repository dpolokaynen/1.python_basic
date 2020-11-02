'''
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type()
для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно,
в программе.
'''
'Создадим переменные каждого сета'
var_int = 5
var_float = 4.3
var_string = 'My world'
var_list = ['thanks', 'for', 'teaching']
var_bool = True
var_tuple = {True, 'date', 19, 10, 2020}
var_set = {'only', 'unique', 'elements'}
var_frozenset = frozenset({'invariable set', 'of unique elements'})
'Проверим тип переменных'
print(type(var_int))
print(type(var_string))
print(type(var_float))
print(type(var_set))
print(type(var_bool))
print(type(var_list))
print(type(var_tuple))
print(type(var_frozenset))
'Сгруппируем в один список'
full_list = {var_string, var_float, var_int, var_bool}
print(full_list)
'Обеъкты типа set не объединяются в списки'
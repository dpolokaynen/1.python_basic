'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''

new_file = open("task_3.txt", "r", encoding='UTF-8')
content = new_file.readlines()
employees_number = len(content)
counter = 0
print(content)
while counter < employees_number:
    employees_data = content[counter].split(sep=' - ')
    income_sum = 0
    income_sum += int(employees_data[1])
    if int(employees_data[1]) < 20000:
        print(employees_data[0])
    counter += 1
print(f'Средний оклад равен {income_sum/employees_number}')
new_file.close()

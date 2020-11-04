'''
 Необходимо создать (не программно) текстовый файл, где каждая строка
 описывает учебный предмет и наличие лекционных, практических и
 лабораторных занятий по этому предмету и их количество.
 Важно, чтобы для каждого предмета не обязательно были все типы занятий.
 Сформировать словарь, содержащий название предмета и общее количество
 занятий по нему. Вывести словарь на экран.
Примеры строк файла:
    Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

task_6 = open('task_6.txt', 'r', encoding='UTF-8')
dictionary = {}
sum_hours = 0
for line in task_6:
    subject = line.split(':')
    print(subject)
    subject_hours = subject[1]
    try:
        lecture_index = subject_hours.index('(л)')
        #print(subject_hours[lecture_index - 3:lecture_index])
        lecture_hours = int(subject_hours[lecture_index - 3:lecture_index])
    except ValueError:
        lecture_hours = 0
    try:
        practise_index = subject_hours.index('(пр)')
        #print(subject_hours[practise_index-3:practise_index])
        practise_hours = int(subject_hours[practise_index - 3:practise_index])
    except ValueError:
        practise_hours = 0
    try:
        lab_index = subject_hours.index('(лаб)')
        #print(subject_hours[lab_index - 3:lab_index])
        lab_hours = int(subject_hours[lab_index - 3:lab_index])
    except ValueError:
        lab_hours = 0
    sum_hours = practise_hours + lecture_hours + lab_hours
    print(sum_hours)
    dictionary[subject[0]] = sum_hours
print(dictionary)
task_6.close()

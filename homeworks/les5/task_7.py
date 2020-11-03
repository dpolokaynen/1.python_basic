'''
Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
 а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить
ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
import json

with open( "task_7.txt", encoding='UTF-8' ) as task_7:
    firms_with_profit = 0
    profit_sum = 0
    result_list = []
    firms_data = {}
    average_profit_dict = {}
    for line in task_7:
        split_line = line.split()
        profit = int(split_line[2]) - int(split_line[3])
        firms_data[split_line[0]] = profit
        if profit >= 0:
            firms_with_profit +=1
            profit_sum +=profit
    average_profit = profit_sum/firms_with_profit
    average_profit_dict["average_profit"] = average_profit
    result_list = [firms_data, average_profit]
    print(result_list)
    task_7_result = open('task_7_result.txt', 'w', encoding='UTF-8')
    json.dump(result_list, task_7_result)

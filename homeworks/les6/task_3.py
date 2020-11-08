'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).Последний атрибут должен быть
защищенным и ссылаться на словарь,содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position
(должность) на базе класса Worker. В классе Position реализовать
методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных
данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 100, 'bonus': 20}
        self.wage = self._income['wage']
        self.bonus = self._income['bonus']
class Position(Worker):
    # def __init__(self, name, surname, wage, bonus):
    #     super().__init__(name, surname, position)
    #     self.name = name
    #     self.surname = surname
    #     self.position = position
    #     self._income['wage'] = wage
    #     self._income['bonus'] = bonus
    def get_full_name(self):
        return print(f'{self.name} {self.surname}')
    def get_total_income(self):
        return print(f'{float(self.wage)+float(self.bonus)}')
test_worker = Position('Petr', 'Petrov','data scientist')
test_worker.get_full_name()
test_worker.get_total_income()

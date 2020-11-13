'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
 Проверить работу полученной структуры на реальных данных.
'''

class Date:
    def __init__(self, date_str):
        date_split = str(date_str).split(sep='-')
        self.day = date_split[0]
        self.month = date_split [1]
        self.year = date_split [2]
        print(date_split)
    @classmethod
    def date_number(cls, date_str):
        date_split = str(date_str).split('-')
        cls.day = int(date_split[0])
        cls.month = int(date_split[1])
        cls.year = int(date_split[2])
        return  cls.day, cls.month, cls.year
    @staticmethod
    def date_validate(date_str):
        date_split = str(date_str).split('-')
        #day = int(date_split[0])
        month = int(date_split[1])
        #year = int(date_split[2])
        if month < 1 or month > 12:
            return 'Неверный месяц'
print(Date.date_number('15-4-1995'))
print(Date.date_validate('15-3-1995'))

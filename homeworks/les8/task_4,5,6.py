'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.А также класс
«Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использоватьстроковый тип
данных. Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум
возможностей, изученных на уроках по ООП
'''

class Office_equipment:
    def __init__(self,name): #type - новая оргетхника или бу
        self.name = name
class Printer(Office_equipment):
    def __init__(self, quantity, color, age, print_type):
        #age - новая оргтeхника или бу
        # print_type - чернобелая печать или цветная
        self.age = age
        self.color = color
        self.print_type = print_type
        super().__init__('printer')
    def __str__(self):
        return f'{self.name}: {self.age},{self.color},{self.print_type}'
class Scaner(Office_equipment):
    def __init__(self, quantity, color, age, scan_type):
        #age - новая оргтехника или бу
        # scan_type - сканирование по 1 странице или сразу несколько
        self.age = age
        self.color = color
        self.scan_type = scan_type
        super().__init__('scaner')
    def __str__(self):
        return f'{self.name}: {self.age},{self.color},{self.scan_type}'
class Xerox(Office_equipment):
    def __init__(self, quantity, color, age, xerox_type):
        #age - новая оргтехника или бу
        # xerox_type - ксерокопирование по 1 странице или сразу несколько
        self.age = age
        self.color = color
        self.xerox_type = xerox_type
        super().__init__('xerox')
    def __str__(self):
        return f'{self.name}: {self.age},{self.color},{self.xerox_type}'

class Store:
    def __init__(self):
        self._equipment_list = {}
    def add_equipment(self, equipment: Office_equipment, quantity):
        value = self._equipment_list.setdefault(type(equipment).__name__)
        if value is None:
            self._equipment_list.update({type(equipment).__name__: quantity})
        else:
            self._equipment_list.update({type(equipment).__name__: value + quantity})
        print(f'На склад поступил товар {equipment} {quantity} шт')

    def sub_equipment(self, equipment: Office_equipment, quantity):
        value = self._equipment_list.setdefault(type(equipment).__name__)
        if value is None:
            raise ValueError('Нет товара на складе')
        if value < quantity:
            print(f'Недостаточно количества товара на складе {quantity-value} шт')
            raise ValueError
        self._equipment_list.update({type(equipment).__name__: value - quantity})
        print(f'Со склада списан {equipment} {quantity} шт')

printer_1 = Printer(1, 'black', 'new','color').__str__()
scaner_1 = Scaner(2, 'white', 'used', 'multi').__str__()
xerox_1 = Xerox(5,'black','new','singe').__str__()
print(printer_1)

store = Store()
store.add_equipment(printer_1,4)
store.add_equipment(scaner_1,3)
store.add_equipment(xerox_1,4)
store.sub_equipment(printer_1,3)
store.sub_equipment(xerox_1,115)
store.add_equipment(scaner_1,3)
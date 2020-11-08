'''
Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних
классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return print('Машина поехала')
    def stop(self):
        return print('Машина остановилась')
    def turn(self, direction):
        self.direction = direction
        return print('Машина повернула', self.direction)
    def show_speed(self):
        return print(f'Текущая скорость равна {self.speed} км/ч')
class TownCar (Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, name, color, is_police=False)
        
    def show_speed(self):
        if self.speed >60:
            return print('Превышение скорости')
        return self.speed
class SportCar (Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, name, color, is_police=False)
    def show_speed(self):
        if self.speed <50:
            return print('Надо ехать быстрее')
        return self.speed
class WorkCar (Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, name, color, is_police=False)
    def show_speed(self):
        if self.speed >40:
            return print('Превышение скорости')
        return self.speed
class PoliceCar (Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, name, color, is_police=True)
        print('Полицейская машина')

test_police = PoliceCar(50,'black','Toyota')
test_sport = SportCar(30,'red','Mazda')
test_sport.show_speed()
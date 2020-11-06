'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния
(красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
'''
import time
import itertools

class TrafficLight:
    __color = 'red'
    __running = 7
    def traffic_change (self, __color, __running):
        if __color == 'red':
            self.__color = 'yellow'
            self.__running = 2
            print(__color)
            time.sleep(__running)
        elif __color == 'yellow':
            self.__color = 'green'
            self.__running = 4
            print(__color)
            time.sleep(__running)
        elif __color == 'green':
            self.__color = 'red'
            self.__running = 7
            print(__color)
            time.sleep(__running)



test_traffic = TrafficLight()
test_traffic.traffic_change()
print(tr)


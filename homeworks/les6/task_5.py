'''
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов методы
должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    def __init__(self, title, draw):
        self.title = title
        self.draw = draw
    def draw_start (self):
        return print('Запуск отрисовки')
class Pen(Stationery):
    def draw_start(self):
        super().draw_start()
        return print('Рисуем ручкой методом', self.draw)

class Pencil(Stationery):
    def draw_start(self):
        super().draw_start()
        return print('Рисуем карандашом методом', self.draw)

class Handle(Stationery):
    def draw_start(self):
        super().draw_start()
        return print('Рисуем маркером методом', self.draw)

test_pen = Pen('Ручка','портрет')
test_pen.draw_start()
test_pencil = Pencil('Карандаш','штриховка')
test_pencil.draw_start()
test_handle = Handle('Маркер','без контура')
test_handle.draw_start()

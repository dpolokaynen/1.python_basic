'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
'''

class My_ZeroDivisionError (Exception):
    @staticmethod
    def division(dividend, divisor):
        try:
            try:
                return dividend / divisor
            except ZeroDivisionError:
                raise My_ZeroDivisionError()
        except My_ZeroDivisionError:
            return f'На ноль делить нельзя'
print(My_ZeroDivisionError.division(2,0))

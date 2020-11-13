'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''

print(f'Мнимую едииниу для комплексных чисел вводить как j. Мнимую часть равную 1 записывать как 1j')
class Complex_number:
    @staticmethod
    def __add__(first_real, first_imaginary, second_real, second_imaginary):
        first_number = complex(first_real, first_imaginary)
        second_number = complex(second_real, second_imaginary)
        return  first_number + second_number
    @staticmethod
    def __mul__(first_real, first_imaginary, second_real, second_imaginary):
        first_number = complex(first_real, first_imaginary)
        second_number = complex(second_real, second_imaginary)
        return first_number * second_number
print(Complex_number.__add__(1,2,-13,-4))
print(Complex_number.__mul__(1,2,-13,-4))

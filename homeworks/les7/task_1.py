'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
 (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
 двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''
class Matrix:
    def __str__(self, content_input):
        strings_input = content_input
        str_matrix = []
        print('Матрица')
        for strings in range(len(strings_input)):
            string = strings_input[strings]
            words = ' '.join([str(elem) for elem in string])

            print(words)
            '''Запишем матрицу в переменную для будущего сложения с ней'''
            str_matrix.append(words)
        print('')
        return str_matrix

    def __add__(self, matrix_1, matrix_2):
        matrix_1_string = Matrix.__str__(self,matrix_1)
        matrix_2_string = Matrix.__str__(self, matrix_2)
        result_matrix = []
        for string in range(len(matrix_1_string)):
            result_str = []
            for element in range(len(matrix_1_string[string])):
                result_element = int(matrix_1_string[string][element]) + int(matrix_2_string[string][element])
                result_str.append(result_element)
                element += 1
            result_matrix.append(result_str)
            string += 1
        return Matrix.__str__(self,result_matrix)

test_matrix = Matrix()
test_matrix.__str__([[123],[456],[789]])
test_matrix.__add__([[111],[222],[333]], [[666],[555],[444]])

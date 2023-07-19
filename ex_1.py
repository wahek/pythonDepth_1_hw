'''
2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
'''
ATTEMPT = 3


def ex_1():
    return check_triangle(input_abc())


def input_abc():
    count = 0
    abc = []
    while True and count < ATTEMPT:
        try:
            a = int(input('Введи сторону a: '))
            abc.append(a)
            b = int(input('Введи сторону b: '))
            abc.append(b)
            c = int(input('Введи сторону c: '))
            abc.append(c)
            return abc
        except ValueError:
            print('Введены неверные данные')
            count += 1


def check_triangle(abc: list):
    max_line = 0
    for i in range(len(abc)):
        if abc[i] > max_line:
            max_line = abc[i]
            index = i
    abc.pop(index)
    if max_line == max(abc):
        return 'Треугольник равнобедренный'
    if max_line < abc[0] + abc[1]:
        if abc[0] == abc[1]:
            if abc[0] == max_line:
                return 'Треугольник равносторонний'
            else:
                return 'Треугольник равнобедренный'
        else:
            return 'Треугольник разносторонний'
    else:
        return 'Треугольника не существует'


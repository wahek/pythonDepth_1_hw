'''
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''

MAX_VALUE = 10000


def ex_2():
    return check_simple(input_number())


def check_simple(num: int):
    count = 0
    for i in range(2, num + 1):
        if num % i == 0:
            count += 1
            if count < 2:
                continue
            else:
                return 'Число составное'
        else:
            continue
    return 'Число простое'


def input_number():
    while True:
        try:
            num = int(input('Введи положительное число не более 10e^5:\n'))
            if MAX_VALUE >= num > 0:
                return num
            else:
                print('Число не может быть отрецательным')
                continue
        except ValueError:
            print('Введено не число')

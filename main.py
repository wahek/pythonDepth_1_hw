import ex_1
import ex_2

while True:
    choice = input('Введи номер задачи: 1, 2:\n')

    match choice:
        case '1':
            print(ex_1.ex_1())
        case '2':
            print(ex_2.ex_2())
        case _:
            print('Пока')
            quit()



from core import *

if __name__ == '__main__':
    rez = input('''1 - Обучение
2 - Прогноз
---> :''')
    if rez == '1':
        num = input('''1 - Свои настройки
2 - Стандартные настройки
---> ''')

        p, e, alpha, N, columns = 0, 0, 0, 0, 0
        if num == '1':
            p = input("Р: ")
            e = input("Е: ")
            alpha = input("А: ")
            N = input("Количество итераций: ")
            columns = input("Столб: ")
        elif num == '2':
            p = 8
            e = 0.00001
            alpha = 0.0001
            N = 100000
            columns = 4

        workout = input("Введите последовательность (1 - 4) для обучения : ")

        training(p, e, alpha, N, columns, int(workout)-1,[100000])

    elif rez == '2':

        print('Введите элементы последовательности')
        print('Enter для завершения ввода"')
        elem = float(input(': '))
        chain = []
        while True:
            try:
                chain.append([elem])
                elem = float(input(': '))
            except:
                break

        number = input("Введите количество прогнозов: ")
        prognosis(chain, int(number))

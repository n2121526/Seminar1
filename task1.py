# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.#

def DayWeek(number):
    if number < 1 or number > 7:
        print('Такого дня недели нет.')
    elif number == 6 or number == 7:
        print('День недели является выходным')
    else:
        print('Этот день недели является будним')

try:
    day = int(input('Введите номер дня недели от 1 до 7 - '))
except:
    print('Надо ввести номер дня недели от 1 до 7!')
    
DayWeek(day)
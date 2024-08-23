def sequence_by_number(number):
    """
    Функция принимает один аргумент,
    определяющий количество элементов в последовательности.
    Инициализируется пустая строковая переменная sequence.
    Циклом перебираем числа от 1 до введеного пользователем.
    Каждое число в цикле преобразуем в строку и повторяем number-раз.
    Добавляем к списку sequence и печатаем number-срез sequence.
    """
    sequence = ''
    for i in range(1, number + 1):
        sequence += str(i) * i
    print(sequence[:number])


if __name__ == '__main__':
    number = int(input('Please, enter number of sequency: '))
    sequence_by_number(number)

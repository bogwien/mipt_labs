# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»,
# а вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».


def prepare_string(val):
    result = ''

    if val % 3 == 0:
        result += 'Fizz'

    if val % 5 == 0:
        result += 'Buzz'

    if result == '':
        result = val

    return result


for number in range(1, 101):
    string = prepare_string(number)

    print(number, ': ', string, sep='')

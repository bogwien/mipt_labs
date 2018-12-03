# Дано натуральное число. Выведите его последнюю цифру.

print('Input number:')
number = str(input())

lastElementIndex = len(number) - 1

print('Last numeral:', number[lastElementIndex] if lastElementIndex > 0 else 'empty')

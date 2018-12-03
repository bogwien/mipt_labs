# Дано натуральное число. Найдите число десятков в его десятичной записи

print('Input number:')
inputData = input()

number = int(inputData) if inputData != '' else 0

tens = (number % 100 - number % 10) / 10
tens = int(tens)

print('Number of tens:', tens)

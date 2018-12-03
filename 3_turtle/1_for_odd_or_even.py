# Для каждого положительного числа, меньшего n, напечатайте odd,
# если число является нечётным, и even, если оно является чётным

print('Input number:')
inputData = input()

number = int(inputData) if inputData != '' else 0

if number > 1:
    for val in range(1, number):
        print(val, 'even' if val % 2 == 0 else 'odd')
else:
    print('Empty')

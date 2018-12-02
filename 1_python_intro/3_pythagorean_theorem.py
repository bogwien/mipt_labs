print('Input leg 1:')
leg1 = int(input())

print('Input leg 2:')
leg2 = int(input())

hypotenuse = round((leg1 ** 2 + leg2 ** 2) ** 0.5, 3)

print('Hypotenuse = sqrt(', leg1, '^2 + ', leg2, '^2) = ', hypotenuse, sep='')

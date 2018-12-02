import math

print('Input x:')
x = int(input())

y = math.log((math.exp(math.sin(x) + 1) * (1.25 + x**-15))**-1, 1 + x**x)

print('Result:', y)

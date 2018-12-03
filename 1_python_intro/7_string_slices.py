# Дана строка. Последовательно на разных строках выведите .. (как в примере)

print('Input string:')
string = str(input())

length = len(string)

print('Third char:', string[2] if length > 2 else 'empty')
print('Penultimate char:', string[-2] if length > 1 else 'empty')
print('First five chars:', string[0:5] if length > 4 else string if length > 0 else 'empty')
print('Without last two chars:', string[0:length - 2] if length > 2 else 'empty')
print('Even chars:', string[::2] if length > 0 else 'empty')
print('Odd chars:', string[1::2] if length > 1 else 'empty')
print('Reversed chars:', string[::-1] if length > 0 else 'empty')
print('Reversed chars through one:', string[::-2] if length > 0 else 'empty')
print('Length:', length)

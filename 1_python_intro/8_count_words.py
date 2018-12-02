print('Input string:')
string = str(input())

wordsNumber = string.count(' ') + 1 if string != '' else 0

print('String has:', wordsNumber, 'words')

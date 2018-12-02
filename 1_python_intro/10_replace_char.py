print('Input string:')
string = str(input())

resultString = 'Input string was empty'

if string != '':
    splitStrIndex = string.find('h') + 1
    replaceLimit = string.count('h') - 2
    resultString = string[:splitStrIndex] + string[splitStrIndex:].replace('h', 'H', replaceLimit)

print('String with replaced h->H:', resultString)

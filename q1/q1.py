from functools import reduce

num = eval(input('How many words: '))
words = []
for n in range(num):
    word = input('Enter word : ')
    words.append(word)

# def shortern(word) : return list(filter(lambda char: char.isupper(), word))

split = list(map(lambda x: list(filter(
    lambda char: char[0].isupper(), x.split(' '))), words))
# shortern = list(map(lambda x: list(map(lambda y: y[x][0], ftr)), ftr))
shortern = []
str = ''
for n in range(0, len(split)):
    for m in range(0, len(split[n])):
        str += split[n][m][0]
    shortern.append(str)
    str = ''
list = sorted(shortern, key=len, reverse=True)
for i in range(len(list)):
    print(list[i])

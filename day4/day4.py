with open('input.txt', 'r') as file:
    lines = file.readlines()
    
lines = [line.replace('\n', '') for line in lines]

###
import string

def parse(line):
    word = list(filter(lambda x: x.isalpha(), line.split('[')[0]))
    start = line.split('[')[0].split('-')[-1]
    end = line.split('[')[-1][: -1]
    count = 100
    for l in end:
        if word.count(l) > count:
            return 0
        else:
            count = word.count(l)
    maxi = max([word.count(c) for c in list(set(string.ascii_lowercase) - set(end)) ])
    if maxi > count:
        return 0
    else:
        return int(start)
        
####

def shift(letter, n):
    return chr( (ord(letter) - 96 + n) % 26 + 96)

def decrypt(line):
    word = list(filter(lambda x: x.isalpha(), line.split('[')[0]))
    start = int(line.split('[')[0].split('-')[-1])
    return ''.join([shift(c, start) for c in word])
    

validLines = list(filter(lambda line: parse(line) > 0, lines))
list(filter(lambda line: decrypt(line).startswith('north'), validLines))
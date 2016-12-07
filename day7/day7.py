### day 6
with open("input.txt", 'r') as file:
    lines = file.readlines()
   
lines = [line.replace("\n", "") for line in lines]
###
def parse(line):
    s1 = line.split('[')
    Out = list(filter(lambda x: "]" not in x, s1))
    In = []
    for part in list(filter(lambda x: "]" in x, s1)):
        Out.append(part.split(']')[1])
        In.append(part.split("]")[0])
    return (In, Out)
    
def isSym(word):
    if len(set(list(word))) != 1:
        return word == word[::-1]
    return False

def haveSym(word):
    n = len(word)
    for start in range(n - 3):
        for step in range(4, int((n - start) // 4 * 4) + 1, 2):
            if isSym(word[start: start + step]):
                return True
    return False

def solve(line):
    In, Out = parse(line)
    return sum(list(map(lambda x: haveSym(x), In))) == 0 and sum(list(map(lambda x: haveSym(x), Out))) > 0
    
print(sum(list(map(lambda line: solve(line), lines))))

###
def isNewSym(word):
    return len(word) == 3 and word[0] == word[2] and word[0] != word[1]

def findSym(word):
    n = len(word)
    output = []
    for start in range(n-2):
        if isNewSym(word[start:start + 3]):
            output.append(word[start:start + 3])
    return output

def getSym(l):
    output = []
    for item in l:
        output.extend(findSym(item))
    return output

def flip(word):
    return word[1] + word[0] + word[1]

def solve1(line):
    In, Out = parse(line)
    symOut = getSym(Out)
    for item in getSym(In):
        if flip(item) in symOut:
            return True
    return False
    
print(sum(list(map(lambda line: solve1(line), lines))))











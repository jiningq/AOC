import hashlib
import time

salt = 'cuanljph'
test = 'abc'

def hash1(input):
    return hashlib.md5(input.encode()).hexdigest()
    
def hash2(input):
    for i in range(2017):
        input = hash1(input)
    return input

def findLetter(hashtext):
    for i in range(len(hashtext) - 2):
        if hashtext[i] == hashtext[i + 1] and hashtext[i + 1] == hashtext[i + 2]:
            return hashtext[i]


def evaluate(i, salt = 'abc', hashfn = hash1):
    hashtext = hashfn(salt + str(i))
    letter = findLetter(hashtext)
    if letter == None:
        return False
    else:
        for j in range(i + 1, i + 1001):
            hashtext = hashfn(salt + str(j))
            if ''.join([letter] * 5) in hashtext:
                return True
        return False

def nthkey(salt, hashfn = hash1, n = 64):
    seen = 0
    guess = 0
    while seen < n:
        guess += 1
        if evaluate(guess, salt, hashfn):
            seen += 1
    return guess

a = time.time()
print(nthkey('abc'))
print(nthkey(salt))
print(time.time() - a)

# part 1 takes 11.7 seconds

###
a = time.time()
print(nthkey('abc', hash2))
print(nthkey(salt, hash2))
print(time.time() - a)

# part 2 takes hours right now, needs speed up



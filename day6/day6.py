### day 6
with open("input.txt", 'r') as file:
    lines = file.readlines()
   
lines = [line.replace("\n", "") for line in lines]
###
def getPos(msg, i):
    vals = [line[i] for line in msg]
    maxVal = ""
    maxFreq = 0
    for v in set(vals):
        if vals.count(v) > maxFreq:
            maxVal = v
            maxFreq = vals.count(v)
    return maxVal

def decode(input):
    return "".join([getPos(input, i) for i in range(len(input[0]))])
    
print(decode(lines))
####
import string

def getPos1(msg, i):
    vals = [line[i] for line in msg]
    minVal = ''
    minFreq = len(msg)
    for l in string.ascii_lowercase:
        if vals.count(l) < minFreq:
            minVal = l
            minFreq = vals.count(l)
    return minVal

def decode1(input):
    return "".join([getPos1(input, i) for i in range(len(input[0]))])

print(decode1(lines))
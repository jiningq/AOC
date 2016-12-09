import time

with open('input.txt') as file:
    msg = file.readlines()

msg = msg[0][:-1]
###
def decompress(msg):
    if '(' not in msg:
        return msg
    else:
        mStart = msg.index('(')
        mEnd = msg.index(')')
        length, times = msg[mStart + 1: mEnd].split('x')
        return msg[:mStart] + msg[mEnd + 1: mEnd + int(length) + 1] * int(times) + decompress(msg[mEnd + int(length) + 1:])
        

print(len(decompress(msg)))

#####
maxDepth = 0

def decompress1(msg, depth = 0):
    global maxDepth
    if depth > maxDepth:
    #    print('Depth:', depth)
        maxDepth = depth
    if '(' not in msg:
        return msg
    else:
        mStart = msg.index('(')
        mEnd = msg.index(')')
        length, times = msg[mStart + 1: mEnd].split('x')
        return msg[:mStart] + decompress1(msg[mEnd + 1: mEnd + int(length) + 1] * int(times), depth + 1) + decompress1(msg[mEnd + int(length) + 1:], depth + 1)
        

a = time.time()
print(len(decompress1(msg)))
print(time.time() - a)

# 10 minutes on a cluster
# 11658395076

###
maxDepth = 0

def dlen(msg, depth = 0):
    global maxDepth
    if depth > maxDepth:
        print('Depth:', depth)
        maxDepth = depth
    if '(' not in msg:
        return len(msg)
    else:
        mStart = msg.index('(')
        mEnd = msg.index(')')
        length, times = msg[mStart + 1: mEnd].split('x')
        return (mStart) + len(decompress1(msg[mEnd + 1: mEnd + int(length) + 1] * int(times))) + dlen(msg[mEnd + int(length) + 1:], depth + 1)

a = time.time()
print(dlen('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'))
print(dlen('(27x12)(20x12)(13x14)(7x10)(1x12)A'))
print(dlen(msg))
print(time.time() - a)

# 8 minutes on a cluster
# 11658395076

####
def sep(msg):
    output = []
    while '(' in msg:
        mStart = msg.index('(')
        mEnd = msg.index(')')
        length, times = msg[mStart + 1: mEnd].split('x')
        if mStart != 0:
            output.append(msg[:msg.index('(')])
        output.append(msg[mStart: mEnd + int(length) + 1])
        msg = msg[mEnd + int(length) + 1:]
    return output

def strip(msg):
    if ')' not in msg:
        return (1, msg)
    mEnd = msg.index(')')
    length, times = msg[1:mEnd].split('x')
    return (int(times), msg[mEnd + 1:])

def dlen(msg):
    if '(' not in msg:
        return len(msg)
    elif len(sep(msg)) == 1:
        stripped = strip(msg)
        return stripped[0] * dlen(stripped[1])
    else:
        return sum(map(lambda x: dlen(x), sep(msg)))

a = time.time()
print(dlen('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'))
print(time.time() - a)
print(dlen('(27x12)(20x12)(13x14)(7x10)(1x12)A'))
print(time.time() - a)
a = time.time()
print(dlen(msg))
print(time.time() - a)

# 0.015 seconds on my laptop
# 11658395076
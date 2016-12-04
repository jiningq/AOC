### day 1
input = 'R3, R1, R4, L4, R3, R1, R1, L3, L5, L5, L3, R1, R4, L2, L1, R3, L3, R2, R1, R1, L5, L2, L1, R2, L4, R1, L2, L4, R2, R2, L2, L4, L3, R1, R4, R3, L1, R1, L5, R4, L2, R185, L2, R4, R49, L3, L4, R5, R1, R1, L1, L1, R2, L1, L4, R4, R5, R4, L3, L5, R1, R71, L1, R1, R186, L5, L2, R5, R4, R1, L5, L2, R3, R2, R5, R5, R4, R1, R4, R2, L1, R4, L1, L4, L5, L4, R4, R5, R1, L2, L4, L1, L5, L3, L5, R2, L5, R4, L4, R3, R3, R1, R4, L1, L2, R2, L1, R4, R2, R2, R5, R2, R5, L1, R1, L4, R5, R4, R2, R4, L5, R3, R2, R5, R3, L3, L5, L4, L3, L2, L2, R3, R2, L1, L1, L5, R1, L3, R3, R4, R5, L3, L5, R1, L3, L5, L5, L2, R1, L3, L1, L3, R4, L1, R3, L2, L2, R3, R3, R4, R4, R1, L4, R1, L5'


steps = input.replace(" ", '').split(',')

import math


l = {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0):(0, 1)}
r = {(-1, 0): (0, 1), (0, -1): (-1, 0), (1, 0): (0, -1), (0, 1): (1, 0)}

def parse(steps):
    (x, y) = (0, 0)
    direction = (0, 1)
    for step in steps:
        #print(step[0])
        if step[0] == 'R':
            direction = r[direction]
        else:
            direction = l[direction]
        #print(step[1])
        distance = int(step[1:])
        x += direction[0] * distance
        y += direction[1] * distance
    return (x, y)

print(parse(steps))

###
# part 2
def findRep(steps):
    (x, y) = (0, 0)
    direction = (0, 1)
    seen = set((0, 0))
    for step in steps:
        #print(step[0])
        if step[0] == 'R':
            direction = r[direction]
        else:
            direction = l[direction]
        distance = int(step[1:])
        for i in range(distance):
            x += direction[0]
            y += direction[1]
            if (x, y) in seen:
                return (x, y)
            else:
                seen.add((x, y))

print(findRep(steps))
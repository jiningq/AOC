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


### day 2
input = '''LRRLLLRDRURUDLRDDURULRULLDLRRLRLDULUDDDDLLRRLDUUDULDRURRLDULRRULDLRDUDLRLLLULDUURRRRURURULURRULRURDLULURDRDURDRLRRUUDRULLLLLDRULDDLLRDLURRLDUURDLRLUDLDUDLURLRLDRLUDUULRRRUUULLRDURUDRUDRDRLLDLDDDLDLRRULDUUDULRUDDRLLURDDRLDDUDLLLLULRDDUDDUUULRULUULRLLDULUDLLLLURRLDLUDLDDLDRLRRDRDUDDDLLLLLRRLLRLUDLULLDLDDRRUDDRLRDDURRDULLLURLRDLRRLRDLDURLDDULLLDRRURDULUDUDLLLDDDLLRLDDDLLRRLLURUULULDDDUDULUUURRUUDLDULULDRDDLURURDLDLULDUDUDDDDD
RUURUDRDUULRDDLRLLLULLDDUDRDURDLRUULLLLUDUDRRUDUULRRUUDDURDDDLLLLRRUURULULLUDDLRDUDULRURRDRDLDLDUULUULUDDLUDRLULRUDRDDDLRRUUDRRLULUULDULDDLRLURDRLURRRRULDDRLDLLLRULLDURRLUDULDRDUDRLRLULRURDDRLUDLRURDDRDULUDLDLLLDRLRUDLLLLLDUDRDUURUDDUDLDLDUDLLDLRRDLULLURLDDUDDRDUDLDDUULDRLURRDLDLLUUDLDLURRLDRDDLLDLRLULUDRDLLLDRLRLLLDRUULUDLLURDLLUURUDURDDRDRDDUDDRRLLUULRRDRULRURRULLDDDUDULDDRULRLDURLUDULDLDDDLRULLULULUDLDDRDLRDRDLDULRRLRLRLLLLLDDDRDDULRDULRRLDLUDDDDLUDRLLDLURDLRDLDRDRDURRDUDULLLDLUDLDRLRRDDDRRLRLLULDRLRLLLLDUUURDLLULLUDDRLULRDLDLDURRRUURDUDRDLLLLLLDDDURLDULDRLLDUDRULRRDLDUDRLLUUUDULURRUR
URRRLRLLDDDRRLDLDLUDRDRDLDUDDDLDRRDRLDULRRDRRDUDRRUUDUUUDLLUURLRDRRURRRRUDRLLLLRRDULRDDRUDLRLUDURRLRLDDRRLUULURLURURUDRULDUUDLULUURRRDDLRDLUDRDLDDDLRUDURRLLRDDRDRLRLLRLRUUDRRLDLUDRURUULDUURDRUULDLLDRDLRDUUDLRLRRLUDRRUULRDDRDLDDULRRRURLRDDRLLLRDRLURDLDRUULDRRRLURURUUUULULRURULRLDDDDLULRLRULDUDDULRUULRRRRRLRLRUDDURLDRRDDULLUULLDLUDDDUURLRRLDULUUDDULDDUULLLRUDLLLRDDDLUUURLDUDRLLLDRRLDDLUDLLDLRRRLDDRUULULUURDDLUR
UULDRLUULURDRLDULURLUDULDRRDULULUDLLDURRRURDRLRLLRLDDLURRDLUUDLULRDULDRDLULULULDDLURULLULUDDRRULULULRDULRUURRRUDLRLURDRURDRRUDLDDUURDUUDLULDUDDLUUURURLRRDLULURDURRRURURDUURDRRURRDDULRULRRDRRDRUUUUULRLUUUDUUULLRRDRDULRDDULDRRULRLDLLULUUULUUDRDUUUDLLULDDRRDULUURRDUULLUUDRLLDUDLLLURURLUDDLRURRDRLDDURLDLLUURLDUURULLLRURURLULLLUURUUULLDLRDLUDDRRDDUUDLRURDDDRURUURURRRDLUDRLUULDUDLRUUDRLDRRDLDLDLRUDDDDRRDLDDDLLDLULLRUDDUDDDLDDUURLDUDLRDRURULDULULUDRRDLLRURDULDDRRDLUURUUULULRURDUUDLULLURUDDRLDDUDURRDURRUURLDLLDDUUDLLUURDRULLRRUUURRLLDRRDLURRURDULDDDDRDD
LLRUDRUUDUDLRDRDRRLRDRRUDRDURURRLDDDDLRDURDLRRUDRLLRDDUULRULURRRLRULDUURLRURLRLDUDLLDULULDUUURLRURUDDDDRDDLLURDLDRRUDRLDULLRULULLRURRLLURDLLLRRRRDRULRUDUDUDULUURUUURDDLDRDRUUURLDRULDUDULRLRLULLDURRRRURRRDRULULUDLULDDRLRRULLDURUDDUULRUUURDRRLULRRDLDUDURUUUUUURRUUULURDUUDLLUURDLULUDDLUUULLDURLDRRDDLRRRDRLLDRRLUDRLLLDRUULDUDRDDRDRRRLUDUDRRRLDRLRURDLRULRDUUDRRLLRLUUUUURRURLURDRRUURDRRLULUDULRLLURDLLULDDDLRDULLLUDRLURDDLRURLLRDRDULULDDRDDLDDRUUURDUUUDURRLRDUDLRRLRRRDUULDRDUDRLDLRULDL'''

steps = input.splitlines()
board1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

board2 = [[0, 0, 1, 0, 0], 
         [0, 2, 3, 4, 0],
         [5, 6, 7, 8, 9],
         [0, 'A', 'B', 'C', 0],
         [0, 0, 'D', 0, 0]]

direc = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

def parse(step, start, board):
    rows, cols = len(board), len(board[0])
    row, col = start
    for c in step:
        move = direc[c]
        if row + move[0] >= 0 and row + move[0] < rows:
            if col + move[1] >= 0 and col + move[1] < cols:
                if board[row + move[0]][col + move[1]] != 0:
                    row += move[0]
                    col += move[1]
    print(board[row][col])
    return (row, col)

# part 1
start = parse(steps[0], (1, 1), board1)
for line in steps[1:]:
    start = parse(line, start, board1)

# part 2
start = parse(steps[0], (2, 0), board2)
for line in steps[1:]:
    start = parse(line, start, board2)

### Day 3
# part 1
with open('input3.txt') as file:
    input = file.readlines()

input = [line.replace('\n', '') for line in input]


def legal(line):
    edges = list(map(lambda x: int(x), filter(lambda x: len(x) > 0, line.split())))
    if edges[0] + edges[1] <= edges[2]:
        return False
    elif edges[0] + edges[2] <= edges[1]:
        return False
    elif edges[1] + edges[2] <= edges[0]:
        return False
    else:
        return True

print(len(list(filter(lambda x: legal(x), input))))

###
# part 2
board = [list(filter(lambda x:len(x) > 0, line.split())) for line in input]
board = [[int(x) for x in line] for line in board]


def getCols(row, col):
    return [board[row][col], board[row + 1][col], board[row + 2][col]]

def listLegal(edges):
    if edges[0] + edges[1] <= edges[2]:
        return False
    elif edges[0] + edges[2] <= edges[1]:
        return False
    elif edges[1] + edges[2] <= edges[0]:
        return False
    else:
        return True

total = 0
for row in range(0, len(input), 3):
    for col in range(3):
        total += int(listLegal(getCols(row, col)))

print(total)


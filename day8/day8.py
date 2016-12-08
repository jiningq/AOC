with open("input.txt", 'r') as file:
    lines = file.readlines()
    
lines = [line.replace('\n', '') for line in lines]

###
board = [[" "] * 50 for i in range(6)]

def rect(x, y):
    for row in range(y):
        for col in range(x):
            board[row][col] = 'O'

def getCol(x):
    return [board[row][x] for row in range(6)]

def rotateCol(x, by):
    col = getCol(x)
    col = col[6 - by:] + col[:6 - by]
    for row in range(6):
        board[row][x] = col[row]

def rotateRow(y, by):
    row = board[y]
    row = row[50 - by:] + row[: 50 - by]
    for col in range(50):
        board[y][col] = row[col]

######
import string

board = [[" "] * 50 for i in range(6)]
for line in lines:
    if line.startswith('rect'):
        x, y = line.split(' ')[1].split('x')
        rect(int(x), int(y))
    elif line.startswith('rotate row'):
        y, by = line.split('=')[1].split(' by ')
        rotateRow(int(y), int(by))
    elif line.startswith('rotate col'):
        x, by = line.split('=')[1].split(' by ')
        rotateCol(int(x), int(by) )

####
print(sum([row.count('O') for row in board ]))

for i in range(6):
    print(''.join(board[i]))

    
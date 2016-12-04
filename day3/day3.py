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
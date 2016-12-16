import random
import itertools

input = {1: ['PrM', 'PrG'], 
         2: ['CoG', 'CuG', 'RG', 'PlG'], 
         3: ['CoM', 'CuM', 'RM', 'PlM'], 
         4: [],
         'E': 1}

exam = {1: ['HM', 'LM'],
        2: ['HG'],
        3: ['LG'],
        4: [],
        'E': 1}


def contain(mom, child):
    if len(child) == 0:
        return True
    return all(map(lambda x: x in mom, child))

def findF(floor, stuff, board):
    return list(map( lambda x: x[:-1], filter(lambda x: x.endswith(stuff), board[floor])))

def isLegal(board):
    for floor in range(1, 5):
        if len(findF(floor, 'G', board)) > 0:
            if not contain(findF( floor, 'G', board), findF(floor, 'M', board)):
                return False
    return True

def getPosMoves(board):
    output = []
    if board['E'] == 1:
        direc = [1]
    elif board['E'] == 4:
        direc = [-1]
    else:
        direc = [1, -1]
    if len(board[board['E']]) == 1:
        for v in direc:
            output.append((board[board['E']],  v))
    else:
        for v in direc:
            for item in board[board['E']]:
                output.append( ([item], v))
            for comb in itertools.combinations(board[board['E']], 2):
                output.append((list(comb), v))
    return output

def doMove(move, board):
    #print('board:', board)
    #print('move:', move)
    toMove = move[0]
    board[board['E']] = list(filter(lambda x: x not in toMove, board[board['E']]))
    board['E'] += move[1]
    board[board['E']].extend(toMove)

def cancelMove(move, board):
    revMove = (move[0], - move[1])
    doMove(revMove, board)
    
##
move = getPosMoves(input)[1]
doMove(move, input)

####

solutions = []

def solve(board, steps = 0):
    print(board, steps)
#    global solution
    if all(map(lambda i:len(board[i]) == 0, range(1, 4))):
        return (board, steps)
    elif steps > 50:
        return None
    else:
        moves = getPosMoves(board)
        for move in moves:
            doMove(move, board)
            if isLegal(board):
                solution = solve(board, steps + 1)
                if solution != None:
                   return solution
            cancelMove(move, board)
        return None
###
solve(exam)
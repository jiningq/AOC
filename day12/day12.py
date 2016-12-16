exam = '''cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''

exam = exam.split('\n')
###
with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = [line.replace('\n', '') for line in lines]
###

def eval(word, env):
    if word.isdigit():
        return int(word)
    else:
        return env[word]

def parse(code, env = {'a': 0, 'b': 0, 'c': 0, 'd': 0}):
    i = 0
    while i < len(code):
        #print(i)
        tokens = code[i].split(' ')
        if tokens[0] == 'cpy':
            tokens = code[i].split(' ')
            env[tokens[2]] = eval(tokens[1], env)
        elif tokens[0] == 'inc':
            env[tokens[1]] += 1
        elif tokens[0] == 'dec':
            env[tokens[1]] -= 1
        elif tokens[0] == 'jnz':
            if eval(tokens[1], env) != 0:
                i += (int(tokens[2]) - 1)
                if i > len(code):
                    return env['a']
        i += 1
        #print(env)
    return env['a']

import time
a = time.time()
print(parse(lines))
print(parse(lines, env = {'a': 0, 'b': 0, 'c': 1, 'd': 0}))
print(time.time() - a)
with open('input.txt', 'r') as file:
    lines = file.readlines()
    
lines = [line.replace('\n', '') for line in lines]

robots = dict()
outputs = dict()

def assign(botNo, val):
    if botNo in robots:
        robots[botNo].append(int(val))
    else:
        robots[botNo] = [int(val)]

givings = []
for line in lines:
    if line.startswith('value'):
        val, botNo = line.split(' ')[1], line.split(' ')[5]
        #print(botNo)
        assign(botNo, val)
    else:
        givings.append(line)

i = 0
while len(givings) > 1:
    #print(i, len(givings))
    words = givings[i].split(' ')
    botNo = words[1]
    if botNo in robots and len(robots[botNo]) == 2:
        if robots[botNo] == [61, 17] or robots[botNo] == [17 , 61]:
            print(botNo)
        if words[5] != 'output':
            assign(words[6], min(robots[botNo]))
        else:
            outputs[words[6]] = min(robots[botNo])
        assign(words[11], max(robots[botNo]))
        robots.pop(botNo, None)
        givings.pop(i)
        i %= len(givings)
    else:
        i = (i + 1) % len(givings)
        
print(comp)
print(outputs['0'] * outputs['1'] * outputs['2'])
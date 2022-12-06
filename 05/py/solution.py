import sys
import copy

def parseInput(inputFile):
    with open(inputFile, 'r') as f:
        raw = f.readlines()
    
    # find the break point between map and moves
    breakline = None
    for i, l in enumerate(raw):
        if len(l) == 1:
            breakline = i
    
    # parse the map first
    nCol = int(raw[breakline - 1][-3])
    nRow = (breakline - 1)

    map = [[] for y in range(nCol)]

    crateIdxs = [i for i in range (5, 100, 4)]
    crateIdxs.insert(0, 1)

    for r in range(nRow-1, -1, -1):
        for c in range(nCol):
            crate = raw[r][crateIdxs[c]]
            if crate != ' ':
                map[c].append(crate)

    # then parse the moves
    # moves will take the form of arrays
    # [quantity, from, to]
    moves = []
    for i in range(breakline+1, len(raw)):
        splitStr = raw[i].split(' ')
        move = [splitStr[1], splitStr[3], splitStr[5].rstrip()]
        move = [int(x) for x in move]
        moves.append(move)
    return map, moves

def solvePart1(map, moves):
    # run the moves
    for move in moves:
        for _ in range(move[0]):
            temp = map[move[1]-1].pop() #indexes in input are 1 indexed
            map[move[2]-1].append(temp)
    result = ""
    for col in map:
        result = result + col[-1]
    return result

def solvePart2(map, moves):
    # run the moves
    for move in moves:
        temp = []
        for _ in range(move[0]):
            temp1 = map[move[1]-1].pop()
            temp.insert(0, temp1)
        map[move[2]-1] = map[move[2]-1] + temp
    result = ""
    for col in map:
        result = result + col[-1]
    return result  


map, moves = parseInput(sys.argv[1])
part1soln = solvePart1(copy.deepcopy(map), moves)
print(f"Part 1 solution is: {part1soln}")
part2soln = solvePart2(copy.deepcopy(map), moves)
print(f"Part 2 solution is: {part2soln}")
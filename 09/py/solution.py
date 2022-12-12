import sys
import numpy as np
import math

def parseInput(fName):
    with open(fName, 'r') as f:
        input = f.readlines()
    inputs = []
    for l in input:
        inputSplit = l.rstrip().split(' ')
        inputs.append([inputSplit[0], inputSplit[1]])
    return inputs

move_dir = {
    "U": [0, 1],
    "D": [0, -1],
    "R": [1, 0],
    "L": [-1, 0]
}

def solvePart1(moves):
    # create a matrix to work in
    mapSize = 500
    tailTouched = np.zeros((mapSize, mapSize))

    start = int(mapSize/2)

    hp = [start, start]
    tp = [start, start]
    tailTouched[tp[1]][tp[0]] = 1

    def calcTailMove():
        dist = math.sqrt(abs(hp[0]-tp[0])**2 + abs(hp[1]-tp[1])**2)
        # tail moves in x and y
        tmx = 0
        tmy = 0
        # they're allowed to be 1 apart, including on the diagonal (which is dist==1.4)
        if dist >= 2.0:
            if (hp[0] > tp[0]):
                tmx += 1
            elif(hp[0] < tp[0]):
                tmx -= 1
            if(hp[1] > tp[1]):
                tmy += 1
            elif(hp[1] < tp[1]):
                tmy -= 1
        return tmx, tmy

    for move in moves:
        mag = int(move[1])
        dir = move[0]
        dx = move_dir[dir][0]
        dy = move_dir[dir][1]

        for i in range(mag):
            hp[0] += dx
            hp[1] += dy
            tmx, tmy = calcTailMove()
            tp[0] += tmx
            tp[1] += tmy
            tailTouched[tp[1]][tp[0]] = 1

    totalTouched = 0
    for ir in range(mapSize):
        for ic in range(mapSize):
            if tailTouched[ir][ic] == 1:
                totalTouched += 1

    return totalTouched

def solvePart2(moves):
    # create a matrix to work in
    mapSize = 500
    tailTouched = np.zeros((mapSize, mapSize))

    start = int(mapSize/2)

    nKnots = 10
    knotPos = []
    for i in range(nKnots):
        knotPos.append([start, start])

    tailTouched[start][start] = 1

    def calcTailMove(knot1idx, knot2idx):
        dist = math.sqrt(
            abs(
                knotPos[knot1idx][0]-knotPos[knot2idx][0]
            )**2 + abs(
                knotPos[knot1idx][1]-knotPos[knot2idx][1]
            )**2)
        # tail moves in x and y
        k2mx = 0
        k2my = 0
        # they're allowed to be 1 apart, including on the diagonal (which is dist==1.4)
        if dist >= 2.0:
            if (knotPos[knot1idx][0] > knotPos[knot2idx][0]):
                k2mx += 1
            elif(knotPos[knot1idx][0] < knotPos[knot2idx][0]):
                k2mx -= 1
            if(knotPos[knot1idx][1] > knotPos[knot2idx][1]):
                k2my += 1
            elif(knotPos[knot1idx][1] < knotPos[knot2idx][1]):
                k2my -= 1
        return k2mx, k2my

    for move in moves:
        mag = int(move[1])
        dir = move[0]
        dx = move_dir[dir][0]
        dy = move_dir[dir][1]

        for i in range(mag):
            knotPos[0][0] += dx
            knotPos[0][1] += dy
            for j in range(nKnots - 1):
                k2mx, k2my = calcTailMove(j, j+1)
                knotPos[j+1][0] += k2mx
                knotPos[j+1][1] += k2my
            tailTouched[knotPos[nKnots-1][0]][knotPos[nKnots-1][1]] = 1

    totalTouched = 0
    for ir in range(mapSize):
        for ic in range(mapSize):
            if tailTouched[ir][ic] == 1:
                totalTouched += 1

    return totalTouched

input = parseInput(sys.argv[1])
part1soln = solvePart1(input)
print(f"Part 1 solution: {part1soln}")
part2soln = solvePart2(input)
print(f"Part 2 solution: {part2soln}")
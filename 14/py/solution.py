import sys
import numpy as np
from copy import deepcopy

# parse the input and return a map of the cave structure
def parseInput(fName):
    with open(fName, 'r') as f:
        raw = f.readlines()
    input =  [l.rstrip() for l in raw]
    # create a full-size map from 0-1000 with a depth of 200 (memory is cheap!)
    # 1 is rock, 2 is sand, 0 is nothing
    cavemap = np.zeros([200, 1000], dtype=np.int8)
    for line in input:
        points = line.split(' -> ')
        points = [[int(j) for j in l.split(',')] for l in points]
        for i in range((len(points)-1)):
            #input is [c,r]
            #left-right line
            if (points[i][0] != points[i+1][0]):
                r = points[i][1]
                c1 = points[i][0]
                c2 = points[i+1][0]
                if c1 > c2:
                    c1, c2 = c2, c1
                for ci in range(c1, c2+1):
                    cavemap[r][ci] = 1
            # vertical line
            else:
                r1 = points[i][1]
                r2 = points[i+1][1]
                c = points[i][0]
                if r1 > r2:
                    r1, r2 = r2, r1
                for ri in range(r1, r2+1):
                    cavemap[ri][c] = 1

    return cavemap

# test that the test input is correct
def testTestInput(input):
    assert input[4][498] == 1
    assert input[5][498] == 1
    assert input[6][498] == 1
    assert input[6][497] == 1
    assert input[6][496] == 1
    assert input[4][503] == 1
    assert input[4][502] == 1

def getLowestRock(cavemap):
    lowestRockR = 0
    for rr in range(len(cavemap)):
        for rc in range(len(cavemap[0])):
            if (cavemap[rr][rc] == 1) and (rr > lowestRockR):
                lowestRockR = rr
    return lowestRockR

def solvePart1(cavemap):
    sandOriginR = 0
    sandOriginC = 500

    sandCount = 0
    # find the lowest rock level (sand below this is in freefall)
    lowestRockR = getLowestRock(cavemap)
    
    while(True):
        sandCount += 1
        sandLocR = sandOriginR
        sandLocC = sandOriginC
        sandMoving = True
        while(sandMoving):
            # check if we're in free fall, return if we are
            if sandLocR > lowestRockR:
                return sandCount - 1
            # not in freefall, let's move some sand
            # nothing below the sand
            if (cavemap[sandLocR + 1][sandLocC] == 0):
                sandLocR += 1
            # next try moving to the left:
            elif (cavemap[sandLocR + 1][sandLocC - 1] == 0):
                sandLocR += 1
                sandLocC -= 1
            # next try moving to the right
            elif (cavemap[sandLocR + 1][sandLocC + 1] == 0):
                sandLocR += 1
                sandLocC += 1
            # sand is stuck
            else:
                # lock the sand's location in the map
                cavemap[sandLocR][sandLocC] = 1
                sandMoving = False

def solvePart2(cavemap):
    sandOriginR = 0
    sandOriginC = 500

    sandCount = 0
    # find the lowest rock level (sand below this is in freefall)
    lowestRockR = getLowestRock(cavemap)

    # fill in the bottom floor of the map (at 2+y = rock)
    for ic in range(len(cavemap[0])):
        cavemap[lowestRockR + 2][ic] = 1

    # run the simulation
    while(True):
        sandCount += 1
        sandLocR = sandOriginR
        sandLocC = sandOriginC
        sandMoving = True
        while(sandMoving):
            # not in freefall, let's move some sand
            # nothing below the sand
            if (cavemap[sandLocR + 1][sandLocC] == 0):
                sandLocR += 1
            # next try moving to the left:
            elif (cavemap[sandLocR + 1][sandLocC - 1] == 0):
                sandLocR += 1
                sandLocC -= 1
            # next try moving to the right
            elif (cavemap[sandLocR + 1][sandLocC + 1] == 0):
                sandLocR += 1
                sandLocC += 1
            # sand is stuck
            else:
                # lock the sand's location in the map
                cavemap[sandLocR][sandLocC] = 1
                sandMoving = False

            if (sandLocC == sandOriginC) and (sandLocR == sandOriginR):
                return sandCount

    


input = parseInput(sys.argv[1])
# testTestInput(input)
part1soln = solvePart1(deepcopy(input))
print(f"Part 1 solution: {part1soln}")
part2soln = solvePart2(deepcopy(input))
print(f"Part 2 solution: {part2soln}")
import sys

def parseInput(fName):
    with open(fName, 'r') as f:
        input = f.readlines()

    input = [l.rstrip() for l in input]
    return input



def solvePart1(input):
    nRows = len(input)
    nCols = len(input[0])
    # map of trees which are visible
    # 1 == visible, 0 == not visible
    visMap = [[0 for i in range(nCols)] for j in range(nRows)]
    
    # set the edges visible
    for ir in range(nRows):
        visMap[ir][0] = 1
        visMap[ir][nCols-1] = 1
    for ic in range(nCols):
        visMap[0][ic] = 1
        visMap[nRows-1][ic] = 1

    # check left<->right first
    for ir in range(1, nRows-1):
        # visibility from left
        lTallest = input[ir][0]
        for ic in range(1, nCols):
            if input[ir][ic] > lTallest:
                visMap[ir][ic] = 1
                lTallest = input[ir][ic]
        # visibility from right
        rTallest = input[ir][nCols-1]
        for ic in range(nCols - 2, 0, -1):
            if input[ir][ic] > rTallest:
                visMap[ir][ic] = 1
                rTallest = input[ir][ic]

    for ic in range(1, nCols-1):
        # visibility from top
        tTallest = input[0][ic]
        for ir in range (1, nRows):
            if input[ir][ic] > tTallest:
                visMap[ir][ic] = 1
                tTallest = input[ir][ic]
        # visibility from bottom
        bTallest = input[nRows - 1][ic]
        for ir in range(nRows - 2, 0, -1):
            if input[ir][ic] > bTallest:
                visMap[ir][ic] = 1
                bTallest = input[ir][ic]

    totalVis = 0
    for ir in range(nRows):
        for ic in range(nCols):
            if visMap[ir][ic] == 1:
                totalVis += 1
    return totalVis

def solvePart2(input):
    nRows = len(input)
    nCols = len(input[0])
    scenicScores = [[0 for i in range(nCols)] for j in range(nRows)]

    def getVisibility(r, c):
        lVis = 0
        rVis = 0
        uVis = 0
        dVis = 0

        # left
        for ic in range(c-1, -1, -1):
            lVis += 1
            if input[r][ic] >= input[r][c]:
                break

        # right
        for ic in range(c+1, nCols):
            rVis += 1
            if input[r][ic] >= input[r][c]:
                break

        # up
        for ir in range(r+1, nRows):
            uVis += 1
            if input[ir][c] >= input[r][c]:
                break

        # down
        for ir in range (r-1, -1, -1):
            dVis += 1
            if input[ir][c] >= input[r][c]:
                break

        return lVis * rVis * uVis * dVis

    maxScore = 0
    for ir in range(nRows):
        for ic in range(nCols):
            scenicScores[ir][ic] = getVisibility(ir, ic)
            if scenicScores[ir][ic] > maxScore:
                maxScore = scenicScores[ir][ic]
    
    return maxScore

input = parseInput(sys.argv[1])
part1soln = solvePart1(input)
print(f"Part 1 solution is: {part1soln}")
part2soln = solvePart2(input)
print(f"Part 2 solution is: {part2soln}")

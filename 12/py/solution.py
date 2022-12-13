import sys
from collections import deque
import numpy as np

def parseInput(fName):
    with open(fName, 'r') as f:
        input = f.readlines()
        input = [l.rstrip() for l in input]

    nRow = len(input)
    nCol = len(input[0])
    starting_pos = []
    ending_pos = []
    map = np.zeros([nRow, nCol])
    for i, row in enumerate(input):
        for j, c in enumerate(row):
            if c == 'S':
                starting_pos = [i, j]
            elif c == "E":
                ending_pos = [i, j]
            else:
                map[i][j] = ord(c) - ord('a')
    return map, starting_pos, ending_pos

def solvePart1(map, start, end):
    nRow = len(map)
    nCol = len(map[0])

    visited = np.zeros((nRow, nCol))

    # store the distance from start and the current coords
    queue = deque([(0, start)])

    while(queue):
        # print(queue)
        d, start = queue.popleft()
        r = start[0]
        c = start[1]
        if visited[r][c] == 1:
            continue
        visited[r][c] = 1
        if start == end:
            return d
        
        max_height = map[r][c] + 1
        min_height = map[r][c] - 1

        # left
        if (c != 0) and (visited[r][c-1] != 1) and (map[r][c-1] <= max_height):
            queue.append((d+1, [r, c-1]))
        # right
        if (c != nCol - 1) and (visited[r][c+1] != 1) and (map[r][c+1] <= max_height):
            queue.append((d+1, [r, c+1]))
        # up
        if (r != 0) and (visited[r-1][c] != 1) and (map[r-1][c] <= max_height):
            queue.append((d+1, [r-1, c]))
        # down
        if (r != nRow - 1) and (visited[r+1][c] != 1) and (map[r+1][c] <= max_height):
            queue.append((d+1, [r+1, c]))

def solvePart2(map, start, end):
    nRow = len(map)
    nCol = len(map[0])

    shortest = 9999999

    map[start[0]][start[1]] = 99999

    def bfs(map, start, end):
        visited = np.zeros((nRow, nCol))

        # store the distance from start and the current coords
        queue = deque([(0, start)])

        while(queue):
            # print(queue)
            d, start = queue.popleft()
            r = start[0]
            c = start[1]
            if visited[r][c] == 1:
                continue
            visited[r][c] = 1
            if start == end:
                return d
            
            max_height = map[r][c] + 1
            min_height = map[r][c] - 1

            # left
            if (c != 0) and (visited[r][c-1] != 1) and (map[r][c-1] <= max_height):
                queue.append((d+1, [r, c-1]))
            # right
            if (c != nCol - 1) and (visited[r][c+1] != 1) and (map[r][c+1] <= max_height):
                queue.append((d+1, [r, c+1]))
            # up
            if (r != 0) and (visited[r-1][c] != 1) and (map[r-1][c] <= max_height):
                queue.append((d+1, [r-1, c]))
            # down
            if (r != nRow - 1) and (visited[r+1][c] != 1) and (map[r+1][c] <= max_height):
                queue.append((d+1, [r+1, c]))

    # find all the 'a' squares
    starts = []
    for i in range(nRow):
        for j in range(nCol):
            if map[i][j] == 0:
                starts.append([i,j])

    for start in starts:
        d = bfs(map, start, end)
        # print(f"Start: {start}, d: {d}")
        if d and (d < shortest):
            shortest = d

    return shortest
    
map, start, end = parseInput(sys.argv[1])
part1soln = solvePart1(map, start, end)
print(f"Part 1 solution: {part1soln}")
part2soln = solvePart2(map, start, end)
print(f"Part 2 solution: {part2soln}")
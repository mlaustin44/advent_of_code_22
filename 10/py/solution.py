import sys
import numpy as np

def parseInput(fName):
    with open(fName, 'r') as f:
        rawinput = f.readlines()
        rawinput = [l.rstrip() for l in rawinput]
    
    input = []
    for l in rawinput:
        if l[0] == 'n':
            input.append(['noop'])
        else:
            splits = l.split(' ')
            input.append(['addx', splits[1]])
    return input

def solvePart1(input):
    # track the state of x
    xs = [1]
    for c in input:
        if c[0] == 'noop':
            xs.append(xs[-1])
        else:
            xs.append(xs[-1])
            xs.append(xs[-1] + int(c[1]))

    idxs = [20, 60, 100, 140, 180, 220]
    sig_sum = 0
    for idx in idxs:
        xval = xs[idx-1]
        sig_sum += xval * idx
    return sig_sum, xs

def solvePart2(input, part1xs):
    SCREEN_H = 6
    SCREEN_W = 40
    screen = np.zeros([6, 40])

    total_ops = len(part1xs)
    for i in range(total_ops):
        current_r = int(i/SCREEN_W)
        current_c = i % SCREEN_W
        if (part1xs[i] - 1 <= current_c) and (part1xs[i] + 1 >= current_c):
            screen[current_r][current_c] = 1
    
    for r in range(SCREEN_H):
        for c in range(SCREEN_W):
            print("#", end='') if (screen[r][c] == 1) else print(' ', end='')
        print(' ')

input = parseInput(sys.argv[1])
part1soln, part1xs = solvePart1(input)
print(f"Part 1 solution is: {part1soln}")
print("\n\nPart 2 solution: \n")
solvePart2(input, part1xs)
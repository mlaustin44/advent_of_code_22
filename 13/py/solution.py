import sys
from functools import cmp_to_key

def parseInput(fName):
    with open(fName, 'r') as f:
        raw = f.readlines()
        input = [l.rstrip() for l in raw]

    packets = []
    for i in range(0, len(input), 3):
        packet1 = eval(input[i])
        packet2 = eval(input[i+1])
        packets.append([packet1, packet2])

    return packets

def comparePackets(p1, p2):
    p1int = isinstance(p1, int)
    p2int = isinstance(p2, int)

    # both ints
    if p1int and p2int:
        return p1 - p2

    # only one is an int
    if (p1int != p2int):
        if p1int:
            return comparePackets([p1], p2)
        else:
            return comparePackets(p1, [p2])

    # both are arrays
    for a, b in zip(p1, p2):
        r = comparePackets(a, b)
        if r != 0:
            return r

    # ran out of comps (like empty arrays in example), so just compare on length
    p1l, p2l = len(p1), len(p2)
    return p1l - p2l


def solvePart1(packets):
    ordered_pkts = []
    for i, packet in enumerate(packets):
        p1, p2 = packet
        result = comparePackets(p1, p2)
        if result < 0: 
            ordered_pkts.append(i+1)
    print(ordered_pkts)
    return sum(ordered_pkts)

        
def solvePart2(packets):
    # slap the packets into one big list
    allpackets = []
    for p in packets:
        allpackets += p

    DEC1 = [[2]]
    DEC2 = [[6]]

    allpackets.append(DEC1)
    allpackets.append(DEC2)

    srt_packets = sorted(allpackets, key = cmp_to_key(comparePackets))

    dec1i = srt_packets.index(DEC1) + 1
    dec2i = srt_packets.index(DEC2) + 1
    return dec1i * dec2i

    

input = parseInput(sys.argv[1])
part1soln = solvePart1(input)
print(f"Part 1 solution: {part1soln}")
part2soln = solvePart2(input)
print(f"Part 2 solution: {part2soln}")
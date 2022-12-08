import sys

class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirs = []
        self.files = []
        self.size = 0
        self.sizeCalced = False
        self.parent = None
    
    def addSubDir(self, subDir):
        self.subdirs.append(subDir)
    
    def addFile(self, file):
        self.files.append(file)

    def setParent(self, parent):
        self.parent = parent

    def calcSize(self):
        for d in self.subdirs:
            if not d.sizeCalced:
                d.calcSize()
                d.sizeCalced = True
        fileTot = sum([x.size for x in self.files])
        dirTot = sum([x.size for x in self.subdirs])
        self.size = fileTot + dirTot


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def parseLs(contents, dir):
    for item in contents:
        # item is a subdirectory
        if item[0] == 'd':
            dirName = item[4:]
            newDir = Directory(dirName)
            newDir.setParent(dir)
            dir.addSubDir(newDir)
        else:
            itemSplit = item.split(' ')
            itemSize = int(itemSplit[0])
            itemName = itemSplit[1]
            newItem = File(itemName, itemSize)
            dir.addFile(newItem)

def parseCommands(commands, rootDir):
    # first command is always "cd /"
    cmd_idx = 1
    current_dir = rootDir
    while (cmd_idx < len(commands)):
        cmd = commands[cmd_idx]
        # command is cd
        if cmd[2:4] == 'cd':
            # go up a level
            if cmd[5:7] == '..':
                current_dir = current_dir.parent
            else:
                target_dir = cmd[5:]
                for dir in current_dir.subdirs:
                    if target_dir == dir.name:
                        current_dir = dir
            cmd_idx += 1
        elif cmd[2:4] == 'ls':
            contents = []
            cmd_idx += 1
            while ((cmd_idx < len(commands)) and (commands[cmd_idx][0] != '$')):
                contents.append(commands[cmd_idx])
                cmd_idx += 1
            parseLs(contents, current_dir)

def parseInput(fileName):
    with open(fileName, 'r') as f:
        contents = f.readlines()
    contents = [x.rstrip() for x in contents]
    return contents

def solvePart1(root):
    root.calcSize()
    dirSizes = []
    def getSizes(dir):
        dirSizes.append(dir.size)
        for d in dir.subdirs:
            getSizes(d)
    getSizes(root)
    total = 0
    for ds in dirSizes:
        if (ds < 100000):
            total += ds

    return total


input = parseInput(sys.argv[1])
rootdir = Directory('/')
parseCommands(input, rootdir)
part1soln = solvePart1(rootdir)
print(f"Part 1 solution is: {part1soln}")
import re

def getCommands(filteredLine):
    # This function finds all "mul(x, y)" patterns in the line
    pattern = r"mul\((\d+),(\d+)\)"
    return re.findall(pattern, filteredLine)

def cleanLine(line):
    newLine = line
    removals = 0
    while "don't()" in newLine:
        # Find the position of "don't()" and "do()"
        remove_start = newLine.find("don't()")
        remove_end = newLine.find("do()", remove_start)
        
        if remove_end == -1:  # No matching "do()" found after "don't()"
            removals+=1
            newLine = newLine[:remove_start]  # Remove everything after "don't()"
        else:
            removals+=1
            partOne = newLine[:remove_start]  # Part before "don't()"
            partTwo = newLine[remove_end + len("do()"):]  # Part after "do()"
            newLine = partOne + partTwo  # Concatenate remaining parts
    print(removals)
    return newLine

#Total input in a line
def lineTotal(line):
    num = 0
    for command in getCommands(line):
        num += int(command[0]) * int(command[1])
    return num

# Read the input file
with open('Input.txt', 'r') as file:
    input = file.read()

#For some reason, don't() commans work disable between lines and it took me an hour to firgure out 
input = input.strip()

print("PartOne - " + str(lineTotal(input)))
print("PartTwo - " + str(lineTotal(cleanLine(input))))

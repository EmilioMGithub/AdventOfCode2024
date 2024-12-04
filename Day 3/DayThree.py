import re

def getCommands(filteredLine):
    # This function finds all "mul(x, y)" patterns in the line
    pattern = r"mul\((\d+),(\d+)\)"
    return re.findall(pattern, filteredLine)

def cleanLine(line):
    while "don't()" in line:
        # Find the position of "don't()" and "do()"
        remove_start = line.find("don't()")
        remove_end = line.find("do()", remove_start)
        
        if remove_end == -1:  # No matching "do()" found after "don't()"
            line = line[:remove_start]  # Remove everything after "don't()"
        else:
            line = line[:remove_start] + line[remove_end + len("do()"):]  # Concatenate remaining parts
    return line

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

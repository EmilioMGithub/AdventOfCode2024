with open('Input.txt', 'r') as file:
    content = file.read()

lines = content.splitlines()

#Checks if it is only increasing
def isGraduallyIncreasing(levels):
  for index in range(len(levels) - 1):
    if levels[index] < levels[index + 1]:
      return False
  return True

#Checks if it is only decreasing
def isGraduallyDecreasing(levels):
  for index in range(len(levels) - 1):
    if levels[index] > levels[index + 1]:
      return False
  return True

#Checks for the adjecent rule, does not check from the edges
def adjacentRule(levels):
  for index in range(len(levels) - 2):
    distanceRight = abs(levels[index + 1] - levels[index + 2])
    distanceLeft = abs(levels[index + 1] - levels[index])
    if distanceRight < 1 or distanceRight > 3:
      return False
    if distanceLeft < 1 or distanceLeft > 3:
      return False
  return True

#Part One loop to check for safe lines
numSafe = 0
for line in lines:
  levels = [int(level) for level in line.split()]
  if adjacentRule(levels) and (isGraduallyIncreasing(levels) or isGraduallyDecreasing(levels)):
    numSafe += 1

print("Part One - " + str(numSafe))

#Loops through the levels by removing it from a modified list and checking if that is safe
def canBeSafeWithDampener(levels):
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if adjacentRule(modified_levels) and (isGraduallyIncreasing(modified_levels) or isGraduallyDecreasing(modified_levels)):
            return True
    return False

#Part 2
numSafe = 0
for line in lines:
  levels = [int(level) for level in line.split()]
  if adjacentRule(levels) and (isGraduallyIncreasing(levels) or isGraduallyDecreasing(levels)):
    numSafe += 1
    continue

  if canBeSafeWithDampener(levels):
    numSafe+=1

print("Part Two - "+str(numSafe))

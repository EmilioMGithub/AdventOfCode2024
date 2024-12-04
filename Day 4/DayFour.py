# Read the input file
with open('Input.txt', 'r') as file:
    input = file.read()

lines = input.splitlines()
matrix = [[lines[outerIndex][innerIndex] for innerIndex in range(len(lines[0]))] for outerIndex in range(len(lines))]

word = "XMAS"
wordLength = len(word)

#I am not commenting part one, this was horrific
rows = len(matrix)
cols = len(matrix[0])

def horizontalLR():
    count = 0
    for row in range(rows):
        for col in range(cols - wordLength + 1):
            if ''.join(matrix[row][col:col+wordLength]) == word:
                count += 1
    return count

def horizontalRL():
    count = 0
    for row in range(rows):
        for col in range(wordLength - 1, cols):
            if ''.join(reversed(matrix[row][col-wordLength+1:col+1])) == word:
                count += 1
    return count

def verticalTB():
    count = 0
    for col in range(cols):
        for row in range(rows - wordLength + 1):
            if ''.join(matrix[row + i][col] for i in range(wordLength)) == word:
                count += 1
    return count

def verticalBT():
    count = 0
    for col in range(cols):
        for row in range(wordLength - 1, rows):
            if ''.join(matrix[row - i][col] for i in range(wordLength)) == word:
                count += 1
    return count

#Diagonal code
rightToLeft = range(wordLength - 1, cols)
leftToRight = range(cols - wordLength + 1)
topToBottom = range(rows - wordLength + 1)
bottomToTop = range(wordLength - 1, rows)

def diagonalTLBR():
    count = 0
    for row in topToBottom:
        for col in leftToRight:
            if ''.join(matrix[row + i][col + i] for i in range(wordLength)) == word:
                count += 1
    return count

def diagonalTRBL():
    count = 0
    for row in topToBottom:
        for col in rightToLeft:
            if ''.join(matrix[row + i][col - i] for i in range(wordLength)) == word:
                count += 1
    return count

def diagonalBLTR():
    count = 0
    for row in bottomToTop:
        for col in leftToRight:
            if ''.join(matrix[row - i][col + i] for i in range(wordLength)) == word:
                count += 1
    return count

def diagonalBRTL():
    count = 0
    for row in bottomToTop:
        for col in rightToLeft:
            if ''.join(matrix[row - i][col - i] for i in range(wordLength)) == word:
                count += 1
    return count

#Call all the methods
wordsFound = (
    horizontalLR() + 
    horizontalRL() + 
    verticalTB() + 
    verticalBT() + 
    diagonalTLBR() + 
    diagonalTRBL() + 
    diagonalBLTR() + 
    diagonalBRTL()
)

print("Part One:"+str(wordsFound))

# ----- Part2 ------

#See if a diagonals starting from a row and col is an x-mas
def checkElement(row, col):
    if(checkDOne(row, col) and checkDTwo(row, col)):
       return True

#Check top left to bottom right diagonal
def checkDOne(row, col):
    if matrix[row][col] == "M":
        if matrix[row+1][col+1] == "A":
            if matrix[row+2][col+2] == "S":
                return True
    if matrix[row][col] == "S":
        if matrix[row+1][col+1] == "A":
            if matrix[row+2][col+2] == "M":
                return True
    return False

#Check bottom left to top right diagonal
def checkDTwo(row, col):
    if matrix[row][col+2] == "M":
        if matrix[row+1][col+1] == "A":
            if matrix[row+2][col] == "S":
                return True
    if matrix[row][col+2] == "S":
        if matrix[row+1][col+1] == "A":
            if matrix[row+2][col] == "M":
                return True
    return False

#Loop through the matrix excluding 2 from the edges
total = 0
for row in range(len(matrix)-2):
    for col in range(len(matrix[0])-2):
        if(checkElement(row, col)):
            total += 1

print("Part Two" + str(total))
#This does not need comments, this first challenge was simple
with open('Input.txt', 'r') as file:
    content = file.read()

lines = content.splitlines()

listOne = []
listTwo = []

for line in lines:
    values = line.split("   ")
    listOne.append(int(values[0]))
    listTwo.append(int(values[1]))

listOne.sort()
listTwo.sort()

total = 0
for index in range(len(listOne)):
    total += abs(listOne[index]-listTwo[index])

print(total)

score = 0
for num in listOne:
    appear = 0
    for numToCheck in listTwo:
        if num == numToCheck: 
            appear+=1
    score+=(num*appear)

print(score)
allNum = []
toDel = []
multiples = []
totalSum = 0

for i in range(1,1000):
    allNum.append(i)

for i in range(len(allNum)):
    if allNum[i] % 3 == 0:
        multiples.append(allNum[i])
        toDel.append(i)
        
for i in range(len(toDel)-1,0, -1):
    allNum.pop(toDel[i])



for i in range(len(allNum)):
    if allNum[i] % 5 == 0:
        multiples.append(allNum[i])

for i in multiples:
    totalSum += i

print(multiples)
print(totalSum)

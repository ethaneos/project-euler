fiveGon = [
    [10,None],
    [None,None],
    [None,None],
    [None,None],
    [None,None]
]
sequenceChecking = 987654321
done = False
def digitCheck(num, digit):
    return str(num).count(str(digit))
def digitsCheck(num):
    for i in range(1,10):
        if digitCheck(num, i)!=1:
            return False
    return True

def newSequence():
    while digitsCheck(sequenceChecking) == False:
        sequenceChecking -= 1

while done == False:
    digitsSequence = list(str(sequenceChecking))
    sums = []
    for i in range(1,5):
        fiveGon[i][1] = digitsSequence[i]
    for i in range(5):
        fiveGon[i][2] = digitsSequence[i+4]
    for i in range(len(fiveGon)):
        sums[i] = sum(fiveGon[i])
    for i in range(len(sums[i])-1):
        if sums[i] != sums[i+1]:
            newSequence()
            break
    print(digitsSequence)
        


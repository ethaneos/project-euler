digits = ["*","0","1","2","3","4","5","6","7","8","9"]
found = False
numChecking = ["*"]

def checkPrime(num):
    posFactor = 2
    while posFactor <= num**(1/2):
        if num % posFactor == 0:
            return False
        posFactor += 1
    return True

def increaseDigit(index):
    for i in index:
        ph1 = (digits.index(numChecking[i]) + 1) % 11
        numChecking[i] = digits[ph1]
    
def increaseNum():
    for j in range(len(numChecking),0,-1):
        increaseDigit([j])
        if numChecking[j] != "*":
            break
        elif j==0:
            numChecking.insert(0, "*")
            break


while found == False:
    varChecking = ""
    primeVar = []
    if "*" not in numChecking:
        continue
    else:
        for k in numChecking:
            varChecking = varChecking + k
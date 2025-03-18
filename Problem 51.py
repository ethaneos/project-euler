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
    posOfStar = []
    primeVar = []
    if "*" not in numChecking:
        increaseNum()
        continue
    else:
        for l in range(0,10):
            for k in range(numChecking):
                if numChecking[k] == "*":
                    posOfStar.append(str(l))
                else:
                    varChecking = varChecking + numChecking[k]
            if checkPrime(int(varChecking)) == True:
                primeVar.append(varChecking)
    if len(primeVar) == 8:
        print(primeVar)
        break
    else:
        increaseNum()

                
            
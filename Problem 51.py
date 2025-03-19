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
    for j in range(len(numChecking)-1,-1,-1):
        increaseDigit([j])
        if numChecking[j] != "*":
            break
        elif j==0:
            numChecking.insert(0, "*")
            break


while found == False:
    primeVar = []
    if "*" not in numChecking:
        increaseNum()
        continue
    else:
        for l in range(0,10):
            varChecking = ""
            for k in range(len(numChecking)):
                if numChecking[k] == "*":
                    if k == 0 and l == 0:
                        break
                    varChecking = varChecking + str(l)
                else:
                    varChecking = varChecking + numChecking[k]
            try:
                if checkPrime(int(varChecking)) == True:
                    primeVar.append(varChecking)
            except:
                continue
    print(primeVar)
    if len(primeVar) == 8:
        print(primeVar)
        break
    else:
        increaseNum()

                
            
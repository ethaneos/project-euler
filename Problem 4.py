palindrome = []

def checkPalindrome(num):
    numStr = str(num)
    numList = list(numStr)
    for k in range(len(numList)):
        if numList[k]==numList[len(numList)-1-k]:
            if k > len(numList)/2:
                return True
            else:
                continue
        else:
            return False
            


for i in range(100,1000):
    for j in range(i,1000):
        if checkPalindrome(i*j) == True:
            palindrome.append(i*j)
        
print(max(palindrome))


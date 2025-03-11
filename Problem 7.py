prime = []
num = 2
done = False

def checkPrime(no):
    for i in prime:
        if no % i == 0:
            return False
    return True

while done == False:
    if checkPrime(num) == True:
        prime.append(num)
    num += 1

    if num % 1000000 == 0:
        print(num)

    if len(prime) == 10001:
        done == True
        print(prime[10000])

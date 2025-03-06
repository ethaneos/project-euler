number = 600851475143
tryDiv = 1
factor = []
prime = []

while True:
    if number % tryDiv == 0:
        if tryDiv <= number/tryDiv:
            factor.append(tryDiv)
            factor.append(int(number/tryDiv))
            tryDiv += 1
        else:
            break
    else:
        tryDiv += 1
print(factor)

for i in factor:
    done = False
    tryDiv = 2
    while done == False:
        if i % tryDiv == 0:
            done = True
        else:
            if tryDiv > i/tryDiv:
                prime.append(i)
                done = True
            else:
                tryDiv += 1
                continue

print(prime)


    

n=232792560
n=1
done = False

def checkDiv(num):
    for i in range(1,21):
        if num % i == 0:
            if i == 20:
                return True
        else:
            return False


while True:
    if checkDiv(n) == True:
        print(n)
        break
    else:
        n+=1
        if n % 10000000 == 1:
            print(n)
print("done")
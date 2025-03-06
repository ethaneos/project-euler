fibonacci = [1,2]
term = 1
evenSum = 0

while fibonacci[term-1] + fibonacci[term] < 4000000:
    fibonacci.append(fibonacci[term-1] + fibonacci[term])
    term+=1
print(fibonacci)

term = 1
while True:
    try:
        evenSum += fibonacci[term]
        term += 3
    except:
        break

print(evenSum)
        

sumsquare = 0
squaresum = 0

for i in range(1,101):
    sumsquare += i**2
    squaresum += i
squaresum **= 2
print(squaresum-sumsquare)
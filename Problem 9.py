for i in range(1000,0,-1):
    for j in range(1,1000-i):
        k=1000-i-j
        if k==0:
            continue
        elif i**2+j**2==k**2:
            print(i,j,k)
            print(i*j*k)
            

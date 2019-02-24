for n in range(2000,3000):
    i=n 
    for j in range(1,5):
        if  n%2==0:
            n=n//10
        elif j==4:
            print(i)
        else:
            break
        
for n in range(2000,3000):
    i=n
    for j in range(1,5):
        if i%2==0:
            i=i//10
            if j==4:
                print(n)
            
        else:
            continue
        

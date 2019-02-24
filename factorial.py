def recur( n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*recur(n-1)
    
    
n=int(input("enter the no to calculate factorial"))
fact=recur(n)
print(fact)

    
            
     
      

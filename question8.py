def binary2decimal(binlist):
    binary1 = str(binlist) 
    decimal, i, n = 0, 0, 0
    while binary1!= 0: 
        dec = int(binary1) % 10
        decimal = decimal + dec * pow(2, i) 
        binary1 = binary1//10
        i += 1
    return decimalno

def isdivisibleby5(decimal):
    if decimal%5==0:
        return 1
    else:
        return 0



if __name__=="__main__": 
    bin=input("enter the binary no separated with  ")
    binlist= bin.split(",")
    decimal=binary2decimal(binlist)
    a=isdivisibleby5(decimal)
    if a==1:
        print("yes")
    else:
        print("no")
    
    
        
    
 
string=input("Enter  the string:")
c1=0
c2=0
for i in string:
      if(i.islower()):
            c1=c1+1
      elif(i.isupper()):
            c2=c2+1
print("The number of lowercase characters is:")
print(c1)
print("The number of uppercase characters is:")
print(c2)
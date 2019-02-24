string=input("Enter string:")
c1=0
c2=0
for i in string:
      if (i.isdigit()):
            c1=c1+1
      elif (i.isalpha()):
            c2=c2+1   
      else:
          continue
print("The number of digits is:")
print(c1)
print("The number of alphabets is:")
print(c2)
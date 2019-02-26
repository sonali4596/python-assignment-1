deposit=0
withdrawl=0
d = input("Enter a deposit amount separated by space ")
list1  = d.split()
w = input("Enter a withdrawl amount separated by space ")
list2  = w.split()
for num in list1:
    deposit += int (num)
for num in list2:
    withdrawl += int (num)
balance=deposit-withdrawl
print(balance)



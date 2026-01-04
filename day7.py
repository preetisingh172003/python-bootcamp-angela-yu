digits=list(map(int,input("enter a number :").split()))
sum = 0
num = int(''.join(map(str, digits)))
for i in digits:
    i=i**3
    sum = sum + i
if sum == num:
    print("ït is armstrong number")
else :
    print("no")


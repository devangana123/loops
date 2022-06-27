num=int(input("enter the number"))
temp=num
sum=0
while temp>0:
    r=temp%10
    sum=sum*10+r
    temp=temp//10
if sum==num:
    print(sum,"is palindrome number")
else:                                                 
    print(sum,"is not palindrome number")
    
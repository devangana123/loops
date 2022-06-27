num=int(input("enter the number:-"))
n=num
rem=0
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
if n%sum==0:
    print(n,"is the harshad number")
else:
    print(n,"is not harshad number")
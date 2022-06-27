# num=int(input("enter the number"))
# decimal=0
# i=0
# while num!=0:
#     a=num%10
#     decimal=decimal+a*pow(2,i)
#     num=num//10
#     i=i+1
# print("decimal number",decimal)


# decimal to binari
# num=int(input("enter the number"))
# bin=0
# p=1
# while num>0:
#     a=int(num%2)
#     bin=bin+a*p
#     p=p*10
#     num=num/2
# print("binary number",bin)





# num=int(input("enter the number"))
# for i in range(num):
#     bin=0
#     p=1
#     n=num
#     while num>0:
#         a=int(num%2)
#         bin=bin+a*p
#         p=p*10
#         num=num/2
# print("binary number",bin)

# num=[0,1,0,3,12]
# i=0
# count=0
# while i<len(num):
#     if num[i]==0:
#         count+=1
#         num.remove(0)
#     i+=1
# for j in range(count):
#     num.append(0)
# print(num)

# # num=int(input("enter the number"))
# n=int("11")
# decimal=0
# i=0
# while n!=0:
#     a=n%10
#     decimal=decimal+a*pow(2,i)
#     n=n//10
#     i=i+1
# # print("decimal number",decimal)
# m=int("1")
# decimal1=0
# i=0
# while m!=0:
#     a1=m%10
#     decimal1=decimal1+a*pow(2,i)
#     m=m//10
#     i=i+1
# num3=(decimal+decimal1)


# decimal to binari
# num=int(input("enter the number"))
# bin=0
# p=1
# while num3>0:
#     a=int(num3%2)
#     bin=bin+a*p
#     p=p*10
#     num3=num3/2
# print("binary number",bin)
















# b_num = list(input("Input a binary number: "))
# value = 0

# for i in range(len(b_num)):
# 	digit = b_num.pop()
# 	if digit == '1':
# 		value = value + pow(2, i)
# print("The decimal value of the number is", value)

# def decimalToBinary(num):
#     if num > 1:
#         decimalToBinary(num // 2)
#     print(num % 2, end='')
# number = int(input("Enter any decimal number: "))
# decimalToBinary(number)     
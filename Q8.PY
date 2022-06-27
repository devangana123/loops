print("you have five chance to guess the numbrer")
print("you have enter the number from 1 to 10")
i=1
while i<=5:
    num=int(input("enter the number"))
    if num==7:
        print("wow,exelent you guess correct number")
        break
    elif num<7:
        print("entered your number is small,try one more time")
    elif num>7:
        print("entered your number is greater,try one more time")
    i+=1
else:
    print("game over")


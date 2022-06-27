print("you have five chance to guess the numbrer")
print("you have enter the number from 1 to 10")
i=1
while i<=5:
    num= int(input("enter the number"))
    if num==9:
        print("exelent you guess correct number")
        break
    else:
        print("your guess is incorrect try again")
    i=i+1
else:
    print("game over")
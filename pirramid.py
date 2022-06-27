num=int(input("enter the number of the row"))
row=0
while row<=num:
    spece=num-row-1
    while spece>=0:
        print(end= " ")
        spece=spece-1
    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    row=row+1
    print() 



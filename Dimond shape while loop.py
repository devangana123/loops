# row=1
# #loop for row
# while row<=4:
#     #loop for spece
#     space=1
#     while space<=4-row:
#         print(' ',end=" ")                                                                                                                
#         space=space+1
#     #loop for star
#     col=1
#     while col<=row*2-1:
#         print("*",end=" ")
#         col=col+1
#     print()
#     row=row+1
# #2nd pattern
# row=3
# #loop for row
# while row>=1:
#     space=1
#     #loop for space
#     while space<=4-row:
#         print("_",end=" ")
#         space+=1
#     #loop for star
#     col=1 
#     while col<=2*row-1:
#         print("*",end=" ")
#         col=col+1
#     print()
#     row=row-1


    
row=1
while row<=4:
    space=1
    while space<=4-row:
        print(' ',end=" ")
        space=space+1
    col=1
    while col<=row*2-1:                                                                                                                                                                
        print("*",end=" ")
        col=col+1
    print()
    row=row+1
row=3
while row>=1:
    space=1
    while space<=4-row:
        print(" ",end=" ")
        space+=1
    col=1 
    while col<=2*row-1:
        print("*",end=" ")
        col=col+1
    print()
    row=row-1


# i=1
# while i<=5:
#     b=5-i
#     while b>0:
#         print(" ",end="")
#         b=b-1
#     j=1
#     while j<=i:
#         print("*", end=" ")
#         j=j+1
#     print()
#     i=i+1
# i=4
# while i>=1:
#     b=5-i
#     while b>0:
#         print(" ",end="")
#         b=b-1
#     j=1
#     while j<=i:
#         print("*", end=" ")
#         j=j+1
#     print()
#     i=i-1
                                
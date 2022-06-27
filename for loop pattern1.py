# for i in range(0,5):                              #1
#     for j in range(i+1):                          #1 2
#         print(j+1,end=" ")                        #1 2 3
#     print()                                       #1 2 3 4
                                                    #1 2 3 4 5
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     print()
#     i=i+1


# num=int(input("enter the number:-"))             #1
# for i in range(1,num+1):                        #212               
#     for j in range(1,num-i+1):                 #32123
#         print(end=" ")                        #4321234   
#     for j in  range(i,0,-1):                 #543212345
#         print(j,end="")
#     for j in range(2,i+1):
#         print(j,end="")
#     print()


# str1=input("enter the sring:-")                     #p
# length=len(str1)                                    #yy
# for i in range(length):                             #ttt
#     for j in range(i+1):                            #hhhh                                                    
#         print(str1[i],end=" ")                      #ooooo
#     print()                                         #nnnnn

 
                           

# str1=input("enter the sring:-")                       #p                        
# length=len(str1)                                      #py
# for i in range(length):                               #pyt
#     for j in range(i+1):                              #pyth
#         print(str1[j],end=" ")                        #pytho
#     print()                                           #python



# str1=input("enter the sring:-")                           #p
# length=len(str1)                                        #p y
# for i in range(length):                               #p y t
#     for j in range (length-i-1):                    #p y t h
#         print(" ",end=" ")                        #p y t h o
#     for j in range(i+1):                        #p y t h o n
#         print(str1[j],end=" ")
#     print()


# str1=input("enter the sring:-")                    #p
# length=len(str1)                                  #y y
# for i in range(length):                          #t t t
#     for j in range (length-i-1):                #h h h h
#         print(" ",end="")                      #o o o o o
#     for j in range(i+1):                      #n n n n n n
#         print(str1[i],end=" ")
#     print()


# str1=input("enter the sring:-")                 #p p p p p p
# length=len(str1)                                #y y y y y
# for i in range(length):                         #t t t t
#     for j in range(length-i):                   #h h h
#         print(str1[i],end=" ")                  #o o
#     print()                                     #n


# str1=input("enter the sring:-")                   #p y t h o n
# length=len(str1)                                  #p y t h o
# for i in range(length):                           #p y t h 
#     for j in range(length-i):                     #p y t
#         print(str1[j],end=" ")                    #p y
#     print()                                       #p


str1=input("enter the sring:-")                     #p y t h o n
length=len(str1)                                      #p y t h o 
for i in range(length):                                 #p y t h
    for j in range(i):                                    #p y t
        print(" ",end=" ")                                  #p y
    for j in range(length-i):                                 #p
        print(str1[j],end=" ")
    print()

# str1=input("enter the sring:-")                     #p p p p p p
# length=len(str1)                                     #y y y y y 
# for i in range(length):                               #t t t t
#     for j in range(i):                                 #h h h
#         print(" ",end="")                               #o o
#     for j in range(length-i):                            #n
#         print(str1[i],end=" ")
#     print()

# str1=input("enter the sring:-")                         #p p p p p p
# length=len(str1)                                          #y y y y y 
# for i in range(length):                                     #t t t t
#     for j in range(i):                                        #h h h
#         print(" ",end=" ")                                      #o o
#     for j in range(length-i):                                     #n  
#         print(str1[i],end=" ")
#     print()

# grocery_list = ['flour','cheese','carrots']
# i=0
# while i<len(grocery_list):
#     print(i,grocery_list[i])
#     i=i+1

# dict1={"key1":1,"key2":2}
# dict2={"key2":2,"key1":1}
# print(dict1==dict2)

# x=0
# a=0
# b=-5
# if a>0:
#     if b<0:
#         x=x+5
#     elif a>5:
#         x=x+4
#     else:
#         x=x+3
# else:
#     x=x+2
# print(x)

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
#     print()
#     i+=1

# k=1
# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end="")
#         b=b+1
#     j=1
#     while j<=k:
#         print("*",end=" ")
#         j=j+1
#     k=k+1
#     print()
#     i=i+1

# a=[[1,2,3,6,5,],[6,5,4,3,5],[8,5,3,2]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if type(a[i])==list:
#             b.append(a[i][j])
#         j=j+1
#     i=i+1
# print(b)


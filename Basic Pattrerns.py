##pattern
##*
##**
##***
##****
##*****
for i in range (6):
    for j in range(i):
        print("*",end="")
    print()

##pattern
##1
##22
##333
##4444
##55555
for i in range (1,6):
    for j in range(0,i):
        print(i,end="")
    print()

##pattern
##1
##12
##123
##1234
##12345
for i in range (1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

##pattern
##1 
##2 3 
##4 5 6 
##7 8 9 10 
##11 12 13 14 15
n=1
for i in range (1,6):
    for j in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print()

import math
def oper():
    choice=int(input("enter ur choice"))
    if choice==1:
        print(a+b)
    elif choice==2:
        print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        print(a/b)
    elif choice==5:
        print(pow(a,b))
    else:
        print("invalid choice")
a=int(input("enter a"))
b=int(input("enter b"))
oper()
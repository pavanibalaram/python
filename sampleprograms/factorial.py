def fact1():
   if n<0:
       return 0
   elif n==1 or n ==0:
       return 1
   else:
       fact=1
       for i in range(1, n+1):
           fact=fact*i
           i+=1
       print("factorial of ", n ,"is", fact)
n=int(input("enter n"))
fact1()

# second method


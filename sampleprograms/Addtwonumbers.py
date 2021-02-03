# first method
a=10
b=5
c=a+b
print(c)

# second method

a=input("enter the value of a")  # it will store the value in strings
b=input("enter the value of b")
print(type(a))
print(type(b))
c=float(a)+float(b) # here values are converted to float
print(type(c))
print("the sum of a and b is", c)
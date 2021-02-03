import math
a=input("enter the value a")
b=input("enter the value b")
c=input("enter the value c")
a=float(a)
b=float(b)
c=float(c)
AreaRT=1/2*a*b
print("area of a right angled triangle", AreaRT)
# area of equilateral triangle
AreaET=1.73*a*a/4
print("area of equiletral triangle", AreaET)
# perimeter of triangle
s=(a+b+c)/2
print("perimeter of triangle", s)
Area=s*(s-a)*(s-b)*(s-c)/2
print("area of a triangle", Area)

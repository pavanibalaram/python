import math
def arm(num):
    n=len(str(num))
    original=num
    res=0
    while(num>0):
        digit=num%10
        res+=digit**n
        num=num//10
    if res==original:
        print("{} is armstrong number" .format(original))
    else:
        print("{} is not a arm strong number" .format(original))
num = int(input("enter a value"))
arm(num)

#  second
n=int(input("enter the range of n"))
for i in range(1,n+1):
    num=i
    count = len(str(i))
    res = 0
    while (i!=0):
        digit = i % 10
        res += digit ** count
        i = i // 10
    if res == num:
        print(res)




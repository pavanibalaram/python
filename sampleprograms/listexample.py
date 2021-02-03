list1=['pavani', 'balaram', 'anuradha', 'bhanu']
print(list1[-3])
print(list1[2])
list1.append('janu') # append will add object at the end  rint()
print(list1)
list1.insert(1,'srivani') # srivani will add at the index 1
print(list1)
list1.remove('pavani')
print(list1)# pavani will remove in the list
print(list1.index('janu'))# it will give the index of janu
print(len(list1)) # it will give length of list
l1=[1,2,3,4,5,1,2,3]
print(l1.count(1)) # it will give count of one's in list
print(l1[::-1]) #reverse the list
print(l1.pop(-3)) # it will deletes the element  at the index
print(l1)
l1.pop()  # it will deletes the element  at the end
print(l1)
for i in l1:
    print(i)
def mystery(a, b=[]):
    b.append(a)
    return b

list1 = mystery(1)
list2 = mystery(2,[])
list3 = mystery(3)


print(list1)
print(list2)
print(list3)
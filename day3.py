a=[1,2,1,1,2,3,4,5,6]

a.extend([8,9])
a.append(7)
print(a[-1::-1]) #reverse a list

#print the smallest elemst from the list
a.sort()
print(a[0])
#print the largest number of the list
a.sort(reverse=True)
rint(a[1])
# how to remove the duplicatye elemet from the list there is no such method is present in python but we use the python set
a=set(a)
print(a)


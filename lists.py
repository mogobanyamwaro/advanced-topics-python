# List orderef,mutable allows dulicates
mylist = ['banaana', 'cherry', 'apple']

mylist2 = list()
print(mylist2)
print(mylist)

item = mylist[0]
print(item)

for i in mylist:
    print(i)

if "banana" in mylist:
    print('yes')
else:
    print('no')

# how many eleemt in lit
print(len(mylist))
mylist.append('lemon')
mylist.insert(1, 'blureberry')

item = mylist.pop()

print(mylist)
item = mylist.remove('cherry')
item = mylist.clear()
mylist.reverse()
mylist.sort()
new_list = sorted(mylist)
# create a new list

mylist2 = [0]*5

mylist3 = [1, 2, 3, 4, 5]
new_list2 = mylist + mylist
# slicing
mylist4 = [1, 2, 3, 4, 5, 6, 6]
a = mylist4[1:5]
# step index
b = mylist4[1:2:4]
# copying the list
list_org = ['Banana', 'apple']
list_copy = list_org
list_copy2 = list_org.copy()

# list comprehesion
c = [1, 2, 3, 4, 5, 6]
d = [i*i for i in a]


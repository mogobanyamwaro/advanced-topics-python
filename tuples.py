# Tuples ordered,immutable allows duplicats elemets

mytuple = ('max', '20', 40)

print(mytuple)
# built in function
mylist = [1,3,4,5,5]
tuples = type(mylist)


item = mytuple[0]
# change the elemts no

for i in mytuple:
    print(i)

if 'max' in mytuple:
    print('yes')
else:
    print('no')


# methods

print(len(mytuple))
print(mytuple.count('20'))
print(mytuple.index('max'))
mylist3 = list(mytuple)
mytuple3 = tuple(mylist3)
# slicing
c = mytuple[2:4]
d =mytuple[2:3:4]
# unpacking
name,age,city = mytuple
# using the star

i1,*i2,i3 = mytuple

# compare a tuple and a list

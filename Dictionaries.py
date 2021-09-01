# key values pairs


mydic = {'name': 'max', 'age': 35, 'cty': "nairobi"}
print(mydic)
value = mydic["name"]
print(value)

mydic['email'] = 'mogoba@gmail.com'
print(mydic)

del mydic['name']
# or
mydic.pop('age')
# or

mydic.popitem()
# chekc if key in dic
if "name" in mydic:
    print('yes')

    # or

try:
    print(mydic['name'])
except:
    print('error')


# loops
for key in mydic.keys():
    print(key)
for value in mydic.values():
    print(value)
for key, value in mydic.items():
    print(key, value)
# same if modify the copy origial is alsloe changed

mydixt_copy = mydic
# good one
mydixt_copy2 = mydic.copy()

# update the dic
mydic.updte(mydixt_copy)

# copy is same
# frozen set, immutable version of set
a = frozenset([1, 2, 3, 4])
# a.u

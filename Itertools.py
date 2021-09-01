# product,combinations.accumulate,groupby, infinite iterators

from itertools import product,permutations,combinations,combinations_with_replacement,accumulate,groupby
# infinite iterators
from itertools import count,cycle,repeat
import operator
a = [1,2,3,4,5]
b = [2]
# prod = product(a,b,repeat=2)
# print(list(prod))


perm = permutations(a,2)
print(list(perm))

comb = combinations(a, func = max())
acc = accumulate(a)

def smaller_than(x):
    return x <3

group_obj = groupby(a,key= smaller_than)


for key,value in group_obj:
    print(key,list(value))

for i in count(10):
    print(i)
    if i ==14:
        break

a=[1,2,3,4]
for i in cycle(a):
    print(i)



for i in repeat(1,4):
    print(i)
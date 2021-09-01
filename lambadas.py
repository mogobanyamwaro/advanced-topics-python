add10 = lambda x:x+10


print(add10(4))




mul = lambda x,y:x*y
print(mul(2,5))

points = [(1,2),(3,4)]
sotted = sorted(points,key= lambda x:x[1])

# map function

a = [1,2,3,4,5,6]
b=map(lambda x:x+2,a)

print(list(b))


# compresion
c = [x*2 for x in a]

# filter
f = filter(lambda x:x%2==0, a)

f1 = [x for x in a if x%2 ==0]

# reduce
from functools import reduce
re =reduce(lambda x,y:x*y,a)
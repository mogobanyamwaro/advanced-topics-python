# import random


# a = random.random()
# a = random.uniform(1, 10)
# a = random.randint(1, 10)
# a = random.randrange(1, 10)
# a = random.normalvariate(0, 1)
mylist = list('abcewiwoidjwoe')

# a = random.choice(mylist)
# a = random.sample(mylist, 3)
# random.shuffle(mylist)

# random.seed(1)
# print(random.random())
# print(random.random())
# print(random.random())

# print(a)

import secrets

a = secrets.randbelow(10)
a = secrets.randbits(4)
a = secrets.choice(mylist)
print(a)

import numpy as np

a = np.random.rand(3,3)
a = np.random.randint(0,10,(3,4))

print(a)



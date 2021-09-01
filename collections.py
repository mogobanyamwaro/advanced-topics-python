# collections:Counter,namedtuple,orderDict,defaultdict,deque

from collections import Counter,namedtuple,OrderedDict,defaultdict,deque


a = 'aaaaabbbbccc'
my_counter = Counter(a)
# print(my_counter.items())
# print(my_counter.values())
# print(my_counter.keys())

# print(my_counter.most_common(1)[0][0])
# print(list(my_counter.elements()))


Point = namedtuple('Point','x,y')
pt = Point(1,-4)
# print(pt)

order_diction = OrderedDict()
order_diction['a']= 1
order_diction['b']= 2
order_diction['c']= 3


d = defaultdict(int)
d['a']=1
d['b']=2
# double ended que
de = deque()
de.append(1)
de.append(2)
de.appendleft(3)
de.pop()
de.popleft()

de.clear()
de.extend([4,5,6])
de.extendleft([4,5,6])
de.rotate(1)
de.rotate(2)
de.rotate(-1)





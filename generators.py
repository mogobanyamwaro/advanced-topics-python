# def mygenerator():
#     yield 1
#     yield 2
#     yield 3

# g = mygenerator()

# # for i in g:
# #     print(i)


# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value)




# print(sum(g))

def fibonnacci (limit):
    a,b = 0,1
    while a<limit:
        yield a
        a,b = b, a+c


fib = fibonnacci(30)
for i in fib:
    print(i)



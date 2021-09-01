
# def start(func):
#     def wrapper(*args,**kwargs):
#         #   before
#         print('start')
#         func(*args,**kwargs)
#         print('before')
#     return wrapper()
       

# @start
# def printName():
#     return print('Douglas')


# printName()
# print_name = start(printName)
# print(print_name)




class CountCalls:
    def __init__(self,func):
        self.func = func
        self.num_calls = 0

        def __call__(self,*args,**kwargs):
            print('hello too')
        

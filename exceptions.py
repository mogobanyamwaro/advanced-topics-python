# raise ex

x = -5

if x < 0:
    raise Exception('x should be positive')


assert(x>0),'x is not positive'

try:
    a = 5/0
    b = a+'10'
except ZeroDivisionError as e:
    print('an error happend',e)

else:
    print('everythin is fine')
finally:
    print('cleaning up')

# define own exception

class ValueTooHighError(Exception):
    pass


def test_value(x):
    if x> 100:
        raise ValueTooHighError(('value is too high'))


try:
    test_value(20)
except ValueTooHighError as e:
    print(e)
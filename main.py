# 9.4

class OopseException(Exception):
    pass

# 1)
try:
    raise OopseException('caught an oops')
except OopseException as err:
    print(err)

# 2)
try:
    raise OopseException()  #()있어도 되고 없어도 가능
except OopseException:
    print('caught an oops')
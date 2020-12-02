
# class test:
#     def mul(c,a,b):
#         return a+b
#
# x=test()
# print(x.mul(10,11))

# class test:
#     x=0
#
# a=test()
# test.x=10
# print(a.x)

class test:
    __data=0

a=test()
a.__data=10
a._test__data=20
test.__data=30
print(test._test__data)
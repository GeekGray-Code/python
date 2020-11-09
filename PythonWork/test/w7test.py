

# def f1(p1,**p2):
#     print(type(p2))
#
# f1(1,a=2)

# def hello():
#     print("hello")
# print(hello())

# i=3
# def f(n=i):
#     print(n)
#
# f()
# i=5
# f()


# def f1(a,b,c):
#     print(a+b)
#
# nums=(1,2,3)
# f1(*nums)



# def f(x,*,y,z):
#     s=x+y+z
#     return s

# f(1,2,3)
# f(x=1,2,z=3)
# f(1,*,2,3)


a=3
def A():
    a=4
    def B():
        global a
        a=5
        print(a)
    B()
    print(a)
A()
print(a)

n=input()

try:
    n=int(n)
    print(10/n)

except ValueError:
    print("Value Error!")

except ZeroDivisionError:
    print("Other exception!")

else:
    print("else is executed!")

finally:
    print("finally is executed!")

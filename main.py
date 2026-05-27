print ("Hello world!")

def divide(a, b):
    print("dividing", a, "by", b)
    return a / b
    print("result is", result)

    return result

try:
    print("before calling divide")
    divide(10, 0)
    print("after calling divide")


except ZeroDivisionError:
    print("cannot divide by zero")
except:
    print("an error occured during division")
else:
    print("division successful")
finally:
    print("finished division operation")

    
# Decorator can enhance the functionality of function
def divide_with_power(func):
    def wrapper(a,b):
        if (b == 0):
            return "Denominator is 0 cannot divide"
        print("Divide Sucessful !!! The result is: ", end="")
        return func(a,b)
    return wrapper

@divide_with_power
def divide(a,b):
    return a / b

print(divide(4,5))
print(divide(4,0))


# @divide_with_power is the systactic sygar of following
# divide = divide_with_power(divide)
# divide(4, 5)

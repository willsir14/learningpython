
def special_operation_2_variables(func):
    def wrapper(a,b):
        return func(a,b)
    return wrapper

@special_operation_2_variables
def add(a,b):
    return a + b

print(add(4, 4))

@special_operation_2_variables
def subtract(a,b):
    return a - b

print(subtract(4,5))

# Decorator = A function that extends the behavior of another function
#              w/o modifying the base function
#              Pass the base function as an argument to the decorator

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    return "Hello!"

print(say_hello())
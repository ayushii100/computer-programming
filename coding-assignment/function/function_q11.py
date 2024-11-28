#Decorator Function
def decorator(func):
    def wrapper():
        print("Function is about to be called!")
        func()
        print("Function call finished!")
    return wrapper

@decorator
def say_hello():
  print("Hello, World!")
say_hello()

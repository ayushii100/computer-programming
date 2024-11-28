#Nested Function
def outer_function(text):
    def inner_function():
        return text.upper()
    return inner_function()
print(outer_function("hello"))

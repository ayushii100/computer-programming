#Checking if string contains only a number
string1 = "12345"
string2 = "12.34"
string3 = "abc123"

is_number1 = string1.isnumeric()  
is_number2 = string2.replace('.', '', 1).isnumeric()  
is_number3 = string3.isnumeric()  

print(f"'{string1}' is numeric: {is_number1}")
print(f"'{string2}' is numeric (float): {is_number2}")
print(f"'{string3}' is numeric: {is_number3}")

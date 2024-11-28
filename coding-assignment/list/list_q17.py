#Find Even and Odd Numbers in a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

 #Count the Frequency of Each Element in a List
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("Frequency of each element:", frequency)

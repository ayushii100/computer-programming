#string padding
word = "Python"
right_justified = word.rjust(10, '*')
print(f"Right justified: {right_justified}")
left_justified = word.ljust(10, '#')
print(f"Left justified: {left_justified}")
centered = word.center(12, '-')
print(f"Centered: {centered}")

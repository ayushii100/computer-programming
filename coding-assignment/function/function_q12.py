#Function with Keyword Arguments
def describe_person(name, age, city="Unknown"):
    return f"{name} is {age} years old and lives in {city}."

print(describe_person("Alice", 30))
print(describe_person("Bob", 25, city="New York"))

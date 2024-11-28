 #Function for Sorting
def sort_by_length(words):
    return sorted(words, key=len)
print(sort_by_length(["apple", "banana", "kiwi", "pear"]))

# program to generate all possible substrings of a given string
def find_substrings(s):
    substrings = set() 
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(s[i:j])
    return sorted(substrings, key=lambda x: (len(x), x))  


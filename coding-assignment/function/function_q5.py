# program to find most frequent character
def most_frequent_char(s):
    from collections import Counter
    s = s.replace(" ", "")  # Remove spaces
    counts = Counter(s)
    most_frequent = counts.most_common(1)[0][0]
    return most_frequent



#String partition
sentence = "apple-orange-banana"
part1, separator, part2 = sentence.partition("-")
print(f"Part before '-': {part1}")
print(f"Separator: {separator}")
print(f"Part after '-': {part2}")

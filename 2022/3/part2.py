import string

lines = open("input").read().splitlines()

total = 0

for idx, line in enumerate(lines):
    if idx % 3 != 0 and idx != 0:
        continue
    (first, second, third) = (line, lines[idx+1], lines[idx+2])
    common_char = [char for char in first if char in second and char in third][0]
    index = string.ascii_lowercase.index(common_char) if common_char in string.ascii_lowercase else string.ascii_uppercase.index(common_char) + 26
    print(index, common_char)
    total += index + 1

print(total)

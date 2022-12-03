import string

lines = open("input").read().splitlines()

total = 0

for line in lines:
    (first, second) = (line[:len(line)//2], line[len(line)//2:])
    common_chars = [char for char in first if char in second]
    # duplicate removal
    common_chars = list(set(common_chars))
    # there seems to be only one common char
    common_char = common_chars[0]
    index = string.ascii_lowercase.index(common_char) if common_char in string.ascii_lowercase else string.ascii_uppercase.index(common_char) + 26
    print(index, common_char)
    total += index + 1

print(total)

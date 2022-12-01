lines = open("input").read().splitlines()

carrying = []

elf = 0
for idx, line in enumerate(lines):
    if not line:
        carrying.append(elf)
        elf = 0
        continue
    elf += int(line)

print(max(carrying))
arrays = {
    "1": "LNWTD",
    "2": "CPH",
    "3": "WPHNDGMJ",
    "4": "CWSNTQL",
    "5": "PHCN",
    "6": "THNDMWQB",
    "7": "MBRJGSL",
    "8": "ZNWGVBRT",
    "9": "WGDNPL"
}

commands = open('input').read().split("\n\n")[1]

for command in commands.splitlines():
    command = command.split()
    print(command)
    amount = -1 * int(command[1])
    stack = command[3]
    dest = command[5]
    crate = arrays[stack][amount:]
    arrays[stack] = arrays[stack][:amount] # remove crate
    arrays[dest] += crate
    print(arrays[dest])
print(arrays)

for idx in arrays:
    print(arrays[idx][-1], end="")

print()
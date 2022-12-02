lines = open("input").read().splitlines()

items = {
    # opponent
    "A": {
        "id": 1,
        "human": "rock",
        "wins": 3,
        "loses": 2
    },
    "B": {
        "id": 2,
        "human": "paper",
        "wins": 1,
        "loses": 3
    },
    "C": {
        "id": 3,
        "human": "scissors",
        "wins": 2,
        "loses": 1
    },
}

total_points = 0

for idx, line in enumerate(lines):
    (enemy, action) = line.split()
    if action == "Y": # draw is required
        total_points += items[enemy]["id"] + 3
    elif action == "X": # lose is required
        total_points += items[enemy]["wins"]
    else: # win is required
        total_points += items[enemy]["loses"] + 6

print(total_points)
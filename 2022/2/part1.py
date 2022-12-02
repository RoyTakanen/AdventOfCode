lines = open("input").read().splitlines()

items = {
    # opponent
    "A": {
        "id": 1,
        "human": "rock",
        "wins": 3
    },
    "B": {
        "id": 2,
        "human": "paper",
        "wins": 1
    },
    "C": {
        "id": 3,
        "human": "scissors",
        "wins": 2
    },
    # me
    "X": {
        "id": 1,
        "human": "rock",
        "wins": 3
    },
    "Y": {
        "id": 2,
        "human": "paper",
        "wins": 1
    },
    "Z": {
        "id": 3,
        "human": "scissors",
        "wins": 2
    },
}

total_points = 0

for idx, line in enumerate(lines):
    (enemy, me) = line.split()
    print(enemy, me)
    total_points += items[me]["id"]
    if items[me]["id"] == items[enemy]["id"]:
        print("Draw:", "me", items[me]["human"], "enemy", items[enemy]["human"])
        total_points += 3
    if items[me]["wins"] == items[enemy]["id"]:
        print("Win:", "me", items[me]["human"], "enemy", items[enemy]["human"])
        total_points += 6
    else:
        print("Lose:", "me", items[me]["human"], "enemy", items[enemy]["human"])

print(total_points)
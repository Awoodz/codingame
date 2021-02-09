# https://www.codingame.com/ide/puzzle/rock-paper-scissors-lizard-spock
from collections import defaultdict

player = []

n = int(input())
for i in range(n):
    inputs = input().split()
    player.append(inputs[1] + inputs[0])

rules = {
    "R": "CL",
    "P": "RS",
    "C": "PL",
    "L": "SP",
    "S": "RC",
}

defeated = defaultdict(list)

while len(player) != 1:
    newplayer = []
    for i in range(int((len(player)) / 2)):

        j = i * 2
        if (
            player[j][:1] not in rules[player[j + 1][:1]]
            and player[j + 1][:1] not in rules[player[j][:1]]
        ):
            winner = (
                [player[j], player[j + 1]]
                if int(player[j][1:]) < int(player[j + 1][1:])
                else [player[j + 1], player[j]]
            )
            newplayer.append(winner[0])
            defeated[winner[0][1:]].append(winner[1][1:])
        else:
            winner = (
                [player[j], player[j + 1]]
                if player[j + 1][:1] in rules[player[j][:1]]
                else [player[j + 1], player[j]]
            )
            newplayer.append(winner[0])
            defeated[winner[0][1:]].append(winner[1][1:])

    player = newplayer.copy()

print(newplayer[0][1:])
print(" ".join(defeated[newplayer[0][1:]]))

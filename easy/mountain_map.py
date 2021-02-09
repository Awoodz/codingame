# https://www.codingame.com/ide/puzzle/mountain-map

n = int(input())  # the number of mountains

height = [int(i) for i in input().split()]
height2 = height.copy()
chaine = []

for j in range(max(height)):
    shape = []
    for i in range(len(height2)):
        up = (
            " " * (height[i] - height2[i]) + "/"
            if height2[i] != 0
            else " " * (height[i] * 2)
        )
        down = "\\" + " " * (height[i] - height2[i]) if height2[i] != 0 else ""
        montagne = up + (" " * (2 * height2[i] - 2)) + down
        shape.append(montagne)
        height2[i] -= 1 if height2[i] > 0 else 0

    chaine.append("".join(shape))

chaine.reverse()
[print(level.rstrip()) for level in chaine]

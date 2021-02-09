# https://www.codingame.com/ide/puzzle/power-of-thor-episode-1
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())
    direction = ""

    y = light_y - initial_ty
    x = light_x - initial_tx

    if y > 0:
        direction += "S"
        initial_ty += 1
    elif y < 0:
        direction += "N"
        initial_ty -= 1

    if x > 0:
        direction += "E"
        initial_tx += 1
    elif x < 0:
        direction += "W"
        initial_tx -= 1

    print(direction)

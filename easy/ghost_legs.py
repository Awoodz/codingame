# https://www.codingame.com/ide/puzzle/ghost-legs
w, h = [int(i) for i in input().split()]
line_list = [input() for i in range(h)]

for i in range(len(line_list[0])):
    if line_list[0][i] != " ":
        startchar = line_list[0][i]
        x, y = (i, 1)
        endchar = line_list[y][x]
        while endchar == "|":
            if x == w - 1:
                if line_list[y][x] == "|" and not (line_list[y][x - 1] == "-"):
                    x, y = (x, y + 1)
                    endchar = line_list[y][x]
                    continue
                elif line_list[y][x - 1] == "-":
                    x, y = (x - 3, y + 1)
                    endchar = line_list[y][x]
            elif x == 0:
                if line_list[y][x] == "|" and not (line_list[y][x + 1] == "-"):
                    x, y = (x, y + 1)
                    endchar = line_list[y][x]
                    continue
                elif line_list[y][x + 1] == "-":
                    x, y = (x + 3, y + 1)
                    endchar = line_list[y][x]
            else:
                if line_list[y][x] == "|" and not (line_list[y][x + 1] == "-" or line_list[y][x - 1] == "-"):
                    x, y = (x, y + 1)
                    endchar = line_list[y][x]
                    continue
                elif line_list[y][x + 1] == "-":
                    x, y = (x + 3, y + 1)
                    endchar = line_list[y][x]
                    continue
                elif line_list[y][x - 1] == "-":
                    x, y = (x - 3, y + 1)
                    endchar = line_list[y][x]
        print(startchar + endchar)
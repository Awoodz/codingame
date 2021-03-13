line = [
    '...#........',
    '...........#',
    '............',
    '............',
    '..#O........',
    '..........#.'
]

x, y = tuple(
    (i, j)
    for i in range(len(line))
    for j in range(len(line[i]))
    if line[i][j] == "O"
)[0]

direction_dict = [
    (x, y - 1),
    (x + 1, y),
    (x, y + 1),
    (x - 1, y),
]

for i in range(10):
    
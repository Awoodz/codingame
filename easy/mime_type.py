# https://www.codingame.com/ide/puzzle/mime-type

n = int(input())
q = int(input())
lext = {}
for i in range(n):
    ext, mt = input().split()
    lext["." + ext.lower()] = mt

fname = [input().lower() for i in range(q)]

for e in fname:
    i_dot = [i for i, char in enumerate(e) if char == "."]
    try:
        print(
            lext[e[max(i_dot):]]
        ) if e[max(i_dot):] in lext else print("UNKNOWN")
    except ValueError:
        print("UNKNOWN")

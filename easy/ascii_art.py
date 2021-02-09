# https://www.codingame.com/ide/puzzle/ascii-art

l = int(input())
h = int(input())
t = input()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
char_nb_list = []

for t_char in t.upper():
    try:
        char_nb_list.append(alphabet.index(t_char))
    except ValueError:
        char_nb_list.append(alphabet.index("?"))

for i in range(h):
    assembled_code = []
    row = input()
    for char_nb in char_nb_list:
        assembled_code.append(row[char_nb*l:(char_nb*l)+l])

    print(*assembled_code[0:len(t)], sep="")

# https://www.codingame.com/ide/puzzle/the-descent

while True:
    mountain_list = [int(input()) for i in range(8)]
    print(mountain_list.index(max(mountain_list)))
    mountain_list.remove(max(mountain_list))

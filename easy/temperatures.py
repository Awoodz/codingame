# https://www.codingame.com/ide/puzzle/temperatures

n = int(input())

lst = [int(i) for i in input().split()]

if lst == []:
    answer = 0
else:
    if min(lst, key=abs) < 0:
        try:
            answer = lst[lst.index(min(lst, key=abs)*-1)]
        except:
            answer = min(lst, key=abs)
    else:
        answer = min(lst, key=abs)

print(answer)

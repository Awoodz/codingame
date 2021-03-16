w, h = [int(i) for i in input().split()]
n = int(input())
x, y = [int(i) for i in input().split()]

xmax, xmin, ymax, ymin = (w, 0, h, 0)

while True:
    bomb_dir = input()
    for char in bomb_dir:
        if char == "R":
            xmin = x
        elif char == "L":
            xmax = x
        elif char == "D":
            ymin = y
        elif char == "U":
            ymax = y
    
    x = int((xmin + xmax)/2)
    y = int((ymin + ymax)/2)

    print(x, y)


# * BELOW : first solution that was uselessly complex

# from math import ceil as mc

# w, h = [int(i) for i in input().split()]
# n = int(input())
# x, y = [int(i) for i in input().split()]

# xr_lim, xl_lim, yu_lim, yd_lim = (w - 1), 0, 0, (h - 1)

# while True:
#     bomb_dir = input()
#     print((bomb_dir, w, h), file=sys.stderr, flush=True)

#     def reward(build_xy, bat_xy, limit):
#         result = (
#             bat_xy - mc((bat_xy)/2)
#             if bat_xy >= 2 
#             else bat_xy - 1
#         )
#         result = result if result >= limit else bat_xy - int((bat_xy - limit)/2)
#         return result

#     def forward(build_xy, bat_xy, limit):
#         result = (
#             bat_xy + int((build_xy - (bat_xy + 1))/2) 
#             if build_xy - (bat_xy + 1) > 1 
#             else bat_xy + mc((build_xy - (bat_xy + 1))/2)
#         )
#         result = result if result <= limit else bat_xy + int((limit - bat_xy)/2)
#         return result

#     rules = {
#         "U": [
#             (x, reward(h, y, yu_lim)),
#             (xr_lim, xl_lim, yu_lim, y),
#         ],
#         "UR": [
#             (forward(w, x, xr_lim), reward(h, y, yu_lim)),
#             (xr_lim, x, yu_lim, y),
#         ],
#         "R": [
#             (forward(w, x, xr_lim), y),
#             (xr_lim, x, yu_lim, yd_lim),
#         ],
#         "DR": [
#             (forward(w, x, xr_lim), forward(h, y, yd_lim)),
#             (xr_lim, x, y, yd_lim),
#         ],
#         "D": [
#             (x, forward(h, y, yd_lim)),
#             (xr_lim, xl_lim, y, yd_lim),
#         ],
#         "DL": [
#             (reward(w, x, xl_lim), forward(h, y, yd_lim)),
#             (x, xl_lim, y, yd_lim),
#         ],
#         "L": [
#             (reward(w, x, xl_lim), y),
#             (x, xl_lim, yu_lim, yd_lim),
#         ],
#         "UL": [
#             (reward(w, x, xl_lim), reward(h, y, yu_lim)),
#             (x, xl_lim, yu_lim, y),
#         ],
#     }

#     if bomb_dir in rules:
        
#         x, y = rules[bomb_dir][0]
#         xr_lim, xl_lim, yu_lim, yd_lim = rules[bomb_dir][1]

#         print(x, y)
#     else:
#         break

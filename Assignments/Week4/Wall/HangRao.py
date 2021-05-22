import math
n = int(input())
built_walls = list(map(int, input().split(' ')))
m = int(input())
other_walls = list(map(int, input().split(' ')))

i = 0
j = 0
max_height = -99999
lst_pos = []
while (i < n):
    # Biên
    if i == 0:
        if built_walls[i] < built_walls[i + 1]:
            while (j < m):
                if built_walls[i] + other_walls[j] == built_walls[i + 1]:
                    lst_pos.append([i + 1, j + 1])
                   
                    if (max_height <= built_walls[i] + other_walls[j]):
                        max_height = built_walls[i] + other_walls[j]
                    
                    built_walls[i] += other_walls[j]

                    j = j + 1
                    break
                j = j + 1
    elif i == n - 1:
        if built_walls[i] < built_walls[i - 1]:
            while (j < m):
                if built_walls[i] + other_walls[j] == built_walls[i - 1]:
                    lst_pos.append([i + 1, j + 1])

                    if (max_height <= built_walls[i] + other_walls[j]):
                        max_height = built_walls[i] + other_walls[j]
                    
                    built_walls[i] += other_walls[j]
                   
                    j = j + 1
                    break
                j = j + 1
    else:
        _min = min(built_walls[i - 1], built_walls[i + 1])
        _max = max(built_walls[i - 1], built_walls[i + 1])
        if built_walls[i] < _min:
            while (j < m):
                if built_walls[i] + other_walls[j] == _min:
                    lst_pos.append([i + 1, j + 1])

                    if (max_height <= built_walls[i] + other_walls[j]):
                        max_height = built_walls[i] + other_walls[j]
                    
                    built_walls[i] += other_walls[j]
                    
                    j = j + 1
                    break
                j = j + 1
        elif built_walls[i] < _max:
            while (j < m):
                if built_walls[i] + other_walls[j] == _max:
                    lst_pos.append([i + 1, j + 1])

                    if (max_height <= built_walls[i] + other_walls[j]):
                        max_height = built_walls[i] + other_walls[j]
                    
                    built_walls[i] += other_walls[j]
                    
                    j = j + 1
                    break
                j = j + 1
    i = i + 1

print(max_height, len(lst_pos))
for pos in lst_pos:
    print(pos[0], pos[1])
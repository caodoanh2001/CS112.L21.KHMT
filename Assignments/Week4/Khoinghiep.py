n, m = list(map(int, input().split(' ')))
rela = []
for i in range(0, m):
    rela.append(list(map(int, input().split(' '))))

dict_rela = {}
for r in rela:
    if r[0] not in dict_rela:
        dict_rela[r[0]] = [r[1]]
    else:
        dict_rela[r[0]].append(r[1])

# find director
i = 0
flg_director = None; 
key_person = list(dict_rela.keys())
while (i < len(dict_rela.keys())):
    print('Xét vị trí', i)
    print('Danh sách thuộc cấp', dict_rela[key_person[i]])
    others = [key for key in key_person[:i] + key_person[i+1:]]
    print('Những người còn lại', others)
    if set(others).issubset(set(dict_rela[key_person[i]])):
        flg_director = i
        break
    i = i + 1


print('Vị trí giám đốc', flg_director)
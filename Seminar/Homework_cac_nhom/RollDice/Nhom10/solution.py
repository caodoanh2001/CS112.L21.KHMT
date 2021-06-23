n, summ = map(int, input().split())

def sol(n, summ):
    if n == 0:
        if summ == 0:
            return 1
        else:
            return 0
    if n < 0:
        return 0
    if n*6 < summ:
        return 0
    if n > summ:
        return 0
    
    count = 0
    for i in range(1,7):
        count += sol(n-1, summ-i)
    return count

print(sol(n,summ))
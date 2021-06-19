def get_result(dices, target):
    if target < dices or target > dices * 6:
        return 0
    if target == dices or target == dices * 6:
        return 1
    dp = [1]
    for d in range(dices):
        newDp = [0] * (min(target, (d+1) * 6) + 1)
        for i in range(1, 6 + 1):
            for j in range(d, len(dp)):
                if i + j >= len(newDp):
                    break
                newDp[i+j] = (newDp[i+j] + dp[j])
        dp = newDp   
    return dp[-1]   

k, n = [int(x) for x in input().split()]

print(get_result(k, n))
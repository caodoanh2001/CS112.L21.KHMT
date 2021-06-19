a, b = list(map(int, input().split()))

def numRollsToTarget(d, target):
    # store number of ways to reach a sum
    # reduce space complexity by only storing previous dice roll
    dp = [0 for _ in range(target + 1)]

    # fill dp array for first dice roll, 1 way to reach each face on die
    for face in range(1, 7):
        if face > target: break
        dp[face] = 1

    # find # ways to reach sums between 1 and target (inclusive) with following dice rolls
    for die in range(1, d):
        new_dp = [0 for _ in range(target + 1)]

        # prefix records sum(dp[max(0,t-f):t])
        # Easy to conceptualize as a sliding window
        prefix = 0
        for t in range(1, target + 1):
            new_dp[t] = prefix

            # slide prefix to the right
            prefix += dp[t]
            if t >= 6:
                prefix -= dp[t - 6]
        dp = new_dp
    return dp[target] % (10 ** 9 + 7)


print(numRollsToTarget(a, b))

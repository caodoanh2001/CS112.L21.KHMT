def giaithua(x):
    if x == 1:
        return 1
    else:
        return x * giaithua(x - 1)

def AmountOfArrangement(array, n):
    ways = giaithua(n)
    count = 1 
    for i in range(n - 1):
        if array[i] == array[i + 1]:
            count += 1
        else:
            ways = ways / giaithua(count)
            count = 1

    ways = ways / giaithua(count)

    return int(ways)

def findWays(array, sum, times, start):

    count = 0
 
    for i in range(start, 7):
        if (times == 0):
            return AmountOfArrangement(array, len(array))
        elif (times == 1):
            if (sum - i == 0):
                array.append(i)
                count = count + findWays(array, sum - i, times - 1, i)
                array = array[:-times]
        elif ((sum - i) / (times - 1)) <= 6:
            array.append(i)
            count = count + findWays(array, sum - i, times - 1, i)
            array = array[:-times]  
 
    return count



# input
k, N = map(int, input().split())
array = []
print(findWays(array, N, k, 1))
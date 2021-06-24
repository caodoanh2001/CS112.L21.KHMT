# Problem 1: BOT

![](https://i.imgur.com/JEviVS7.png)

Below we will describe clearly our solution

**Abstraction**: Find the subarray that has largest total sum.

**Pattern Recognition**: Dynamic Programming

**Pesudocode**:

```[python3]
Given arr[n]

Begin from first element (start = 0)
for i:=0 to n-1:
    current_sum <- current_sum + arr[i] (cumulative sums)
    if current_sum > max_sum: (check whether current cumulative sums larger than cumulative max sums)
        max_sum <- current_sum (tracking current cumulative sums)
        position_start <- start (update index of first element of subarray)
        position_end <- i (update index of last element of subarray)
        
    if current_sum < 0: (check whether current cumulative sum is negative)
        position_start <- i + 1 (we will update the index of first element of subarray to the next element of original array.)
        current_sum <- 0 (we will remove cumulative sum, calculate it again from the next element.)

return position_start, position_end, max_sum
    
```

**Complexity**: O(n). 
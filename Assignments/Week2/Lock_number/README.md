# Lock_number

## Problem

To increase the safety against bank robbery, people use digital keys with a simple but very effective unlock code. A fairly long string of digits was displayed on the door. Digits can be swapped or deleted. To unlock one has to move the digits and, if necessary - delete a few digits to get the largest string that satisfies the set condition. This condition is changed frequently. Today the condition is "The received number must be divisible by 3". The received number may start with digits 0. The string "000" is larger than the string "00".

Identify the key to open the door.

**Input:**

- Number **n** contains **k** digits (**n** < 10<sup>5</sup>, **k** > 2)

**Output:**

- Largest **key** number multiple of 3

Example:


<table>
<tbody>
<tr>
<td>Input</td>
<td>Output</td>
</tr>
<tr>
<td>
105
</td>
<td>
510
</td>
</tr>
</tbody>
</table>

## Abstraction

Rearrange and remove **k** digits in a number to find the largest number multiple of 3

## Pattern Recognition

Divide and Conquer

## Algorithm designed

Below we describe our pesudocode for this problem:

```
function solve(arr): 
    arr <- sorted(arr) (sort non-decreasing)
    queue0 <- [] (digit % 3 == 0)
    queue1 <- [] (digit % 3 == 1)
    queue2 <- [] (digit % 3 == 2)
    for i in arr:
        sum <- sum + i
        if (i % 3 == 0):
            Add i to queue0
        else
            if (i % 3 == 1):
                Add i to queue1
            else:
                Add i to queue2
            endif
        endif
    endfor
            
    if (sum % 3 == 1):
        if queue1:
            queue1 <- queue1[1:]
        else: 
            if queue2:
                queue2 <- queue2[2:] ( (2+2)%3 == 1 )
            endif
        endif

    else
        if (sum % 3 == 2):
            if queue2:
                queue2 <- queue2[1:] 
            else 
                if queue1:
                    queue1 <- queue1[2:]
                endif
            endif
        endif
    endif
            
    aux <- queue0 + queue1 + queue2 (merge all digits list)
    aux <- sorted(aux)
    aux <- reverse(aux) (reverse array)
    return aux
```

## Complexity

- **Sorting:** Timsort - O(n.log(n))
- **Algorithm:** O(n)

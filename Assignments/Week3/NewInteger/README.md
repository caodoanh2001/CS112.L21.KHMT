# New Integer

## Problem

Let a positive integer n have no more than 100 digits. Find the largest integer m is divisible by 3 and differs from n by exactly one digit.

Input from standard input device:

Data: Input a positive integer n have no more than 100 digits which don't have meaningless 0 digits. 

Example:


<table>
<tbody>
<tr>
<td>Input</td>
<td>Output</td>
</tr>
<tr>
<td>
<p><tt>123</tt></p>
</td>
<td>723</td>
</tr>
</tbody>
</table>

## Abstraction

Given integer n, try to find integer m so that m is divisible by 3, different from n 1 digit, and as large as possible.

## Pattern Recognition

Brutal Force

## Algorithm designed

The main idea is search all solutions that divisible by 3 and and differs from n by exactly one digit. After that, we put these into a list and find the largest solution.

```
function divisiblebyK(n):
    str_n <- string(n)
    int_n <- int(n)
    rs <- [] # list that contains all solutions which divisible by 3 and and differs from n by exactly one digit
    for i:=1 to n: # Loop and find solutions
        int_n <- int_n - int(str_n[i])
        N <- (3 - (int_n % 3)) % 3
        for j:=N to 3:
            j <- j*3
            if (j != int(str_n[i])):
                t <- (str_n[0:i] + str(j) + str_n[i+1:])
                Add t to rs
            endif
        endfor
        int_n <- int_n + int(str_n[i])
    endfor

    rs <- sort(rs) # Sort list from small to large
    idx <- len(rs)-1 # get idx final item
    return rs[idx] # the largest is th
```

## Complexity

Complexity: O(N*10)
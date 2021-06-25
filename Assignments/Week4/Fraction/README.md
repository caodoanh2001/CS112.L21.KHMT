## Problem
![](https://i.imgur.com/9gqhqvF.png)

## Abstraction 

Find the number of times **a/b** is converted to **c/d** with each transformation increasing the numerator and denominator by 1, and then simplifying the fraction. 

## Patern Recognition

Brute Force

## Algorithm designed

First we create n and set it to 0 for storing times. Then we follow steps below:
1. Check 3 conditions:
    - a x d <= b x c (whether a/b can be converted to c/d)
    - a/b < 1 (not larger than 1)
    - c/d < 1 (not larger than 1)
2. Run a while loop:
    2.1. Increase a and b by 1.
    2.2. Caculate greatest common divisor of a and b.
    2.3. Increase n by 1.
    2.4. If we find the step that the value of a,b equal to c,d respectively, we return n.

```
Given a,b,c,d
function(a,b,c,d):
    n <-- 0
    if (a*d <= b*c and a/b < 1 and c/d < 1)):
        while (a*b < c*d):
            a <-- a + 1         // increase a by 1
            b <-- b + 1        // increase b by 1
            cd <-- GCD(a, b)    // Calculate greatest common divisor of a and b.
            n <-- n + 1        // increase the times
            if (a==c and b==d):
                return n
            endif
        endwhile
    endif
```

## Complexity

Because of using a while loop, complexity is O(n). In step 2.2 we calculate the GCD of a and b by **gcd** function of **math** library, if they use Euclidean algorithm for this function, complexity is O(n). Combine 2 complexities we may figure out the complexity of this solution is **O(n^2)**
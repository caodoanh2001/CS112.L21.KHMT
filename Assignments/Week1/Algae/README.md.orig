# Problem 2: Algae

Below we will describe clearly our solution

Let's consider n = 1, we will observe the growth process of algaes.

- Day 0 (k = 0): <b>1</b> algae level 1
- Day 1 (k = 1): <b>1</b> algae level 1, <b>1</b> algae level 2
- Day 2 (k = 2): <b>3</b> algaes level 1, <b>1</b> algae level 2, <b>1</b> algae level 3
- Day 3 (k = 3): <b>8</b> algaes level 1, <b>3</b> algaes level 2, <b>1</b> algae level 3, <b>1</b> algae level 4
- Day 4 (k = 4): <b>21</b> algaes level 1, <b>8</b> algaes level 2, <b>3</b> algaes level 3, <b>1</b> algae level 4, <b>1</b> algae level 5

After observing, we find that the algae growth is in compliance with the rule. Now let's compare the Fibonacci sequence:

As we knew, call F(n) is n-th Fibonacci number:
F(n) = F(n-1) + F(n-2) with n > 2

|       i-th       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7  | 8  | 9  | ... |
|:----------------:|---|---|---|---|---|---|---|----|----|----|-----|
| Fibonacci number | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | ... |

More observation, we can figure out the number of algaes at k-th day is exactly the (2k+1)th fibonacci number!

It means we can summary this problem by following:

**Abstraction**: Given n and k, calculate (2k+1)th fibonacci number and multiply it with n.

**Pattern Recognition**: Fibonacci number

**Algorithm designed**:

#### Naive approach
Fibonacci number is a familiar problem in programming. An usual way that can be implemented immediately that use recursion but this solution may become useless with extremely large n-th, so we have to move on another way.

#### Effective approach
To deal with large number of n, we can use power of the matrix M = [[1,1],[1,0]]
The idea is based on the fact that if we multiply n times matrix M with itself (M to the power of n), we will receive (n+1)-th fibonacci number at current M[0][0]. The image of expression below we describe more clearly.

![](https://i.imgur.com/tTs8hoc.png)

#### Complexity: O(n)
#### Pedosuecode
First, we define base `fib()` function:

```
Given index of n

<<<<<<< HEAD
function fib(n):
=======
fib(n):
>>>>>>> 076f92f02d11ab0510e88210c3a9852a30d0ca80
    F <- [[1,1],
        [1,0]]
    
    F <- power(F, n-1)
    return F[0][0]
        
```

Second, we define helper function that can calulate the power of matrix.

```
Given base matrix F, k power

function power(F,k):
    # We define again the matrix for the purpose of multiplication.
    M <- [[1,1],
        [1,0]]
    for i:= 0 to n-1:
        F <- multiply(F,M)
<<<<<<< HEAD
    endfor
=======
>>>>>>> 076f92f02d11ab0510e88210c3a9852a30d0ca80
    return F
```

Third, we define another helper function that can calulate the multiplication between two matrixs:

```
Given matrix A, B
<<<<<<< HEAD
function multiply(A, B):
=======
multiply(A, B):
>>>>>>> 076f92f02d11ab0510e88210c3a9852a30d0ca80
    F_0_0 <- (F[0][0] * M[0][0] + F[0][1] * M[1][0])
    F_0_1 <- (F[0][0] * M[0][1] + F[0][1] * M[1][1])
    F_1_0 <- (F[1][0] * M[0][0] + F[1][1] * M[1][0])
    F_1_1 <- (F[1][0] * M[0][1] + F[1][1] * M[1][1])
     
    F[0][0] <- F_0_0
    F[0][1] <- F_0_1
    F[1][0] <- F_1_0
    F[1][1] <- F_1_1
    
    return F
```

That's it! Now combine all functions:

```
Given number of algae n and k-th day

<<<<<<< HEAD
function algae(n, k):
=======
algae(n, k):
>>>>>>> 076f92f02d11ab0510e88210c3a9852a30d0ca80
    i_th <- 2*k+1
    result_at_k_th_day <- n * fib(i_th)
    return result_at_k_th_day
```

# H_index

## Problem

How do you measure a scientist's success? Based on the number of articles published or on the number of times an article has been cited in the work of others? Both of those parameters are important.

An article has a citation score of **c** if it is cited **c** times in the works of other scientists. One of the ways to evaluate a scientist's success is to calculate the **H_Index** impact index based on the combination of the number of articles and the citation index of those articles.

A scientist's **H_Index** is maximum of **k** if he or she has **k** articles, each with a citation score of not less than **k**. For example, if a person has 10 articles, each of which is cited no less than 10 times, that person's **H_Index** is at least equal to 10.

A person has **n** articles, the **i-th** article has the citation score of **c_i**, *i = 1 ÷ n*. Identify that person's **H_Index**.

Input from standard input device:

- The first line contains an integer n (1 ≤ n ≤ 5 × 105),
- Line 2 contains n integers **c1**, **c2**,..., **cn** (0 ≤ ci ≤ 106, i = 1 ÷ n).
- **Result:** Give the standard output an integer - found **H_index**

Example:


<table>
<tbody>
<tr>
<td>Input</td>
<td>Output</td>
</tr>
<tr>
<td>
<p><tt><strong>5</strong></tt></p>
<p><tt><strong>8 5 3 4 10</strong></tt></p>
</td>
<td>4</td>
</tr>
</tbody>
</table>

## Abstraction

Find the largest **k** number that is equal to or less than **k** components in an array.

## Pattern Recognition

Loop
Array sorting

## Algorithm designed

Below we describe our pesudocode for this problem:

```
count = 0
i = 0 
last = n (In the begining, possible max of k is n)
while i < n: (check if i is still less than n)
    if cites[i] >= last: (check if i-th component is greater than number of articles)
        count = count + 1 (if it is, increase count by 1)
    else:
        last = last - 1 (if not, decrease possible max of k by 1)
    i = i + 1
```

## Complexity

Because the worst case is checking all components in an array, so the complexity is **O(n)**
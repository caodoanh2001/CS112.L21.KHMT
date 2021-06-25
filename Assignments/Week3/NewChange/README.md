# New change

## Problem

The city decided to cut down all existing trees in the city to plant only one new tree. The task is assigned to the City Green Tree Company. Due to equipment limitation, the Company can organize only two teams to cut down trees. Team I kills a tree every day, but every kth day, they have to rest for technical maintenance, that is, team I will rest on days ***k***, ***2k***, ***3k***,. . . Team II cuts down b trees every day, but every mth day, they have to rest for technical maintenance. That means Team II will rest on days ***m***, ***2m***, ***3m***,. . . On the day off, the number of felling trees for the team will be 0. Both teams start work on the same day and work in tandem. 

Input from standard input device:

Data: Input from the standard input device consists of a line containing 5 integers **a**, **k**, **b**, **m** and **n** (1 ≤ **a**, **b** ≤ 109, 2 ≤ **k**, **m** ≤ 1018, 1 ≤ **n** ≤ 1018). 

Example:


<table>
<tbody>
<tr>
<td>Input</td>
<td>Output</td>
</tr>
<tr>
<td>
<p><tt><strong>2 4 3 3 25</strong></tt></p>
</td>
<td>7</td>
</tr>
</tbody>
</table>

## Abstraction

We have the number of working days of team I is ![](https://i.imgur.com/JU4TRvP.png)
, with ![](https://i.imgur.com/zlCddGk.png) is an integer.
the number of working days of team II is ![](https://i.imgur.com/SGob5Vp.png), with ![](https://i.imgur.com/Ryo3SOS.png) is an integer.
Therefore, total trees that both teams grow:
![](https://i.imgur.com/wtdIwzj.png)
So that we have to find the minimum of ![](https://i.imgur.com/aa15hgt.png) that still less than or equal the value of below equation:
![](https://i.imgur.com/vINkIbg.png)


## Pattern Recognition

Dynamic programming

## Algorithm designed

The main idea is search the value of x from 0 to inf.

## Complexity

This is essentially a binary search algorithm so that the complexity is **O(log(n))**

![](https://i.imgur.com/Cvgw9lZ.png).
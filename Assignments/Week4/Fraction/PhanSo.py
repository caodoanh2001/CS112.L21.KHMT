import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())

def solve(a,b,c,d):
    n = 0
    if (a*d < b*c and c/d < 1 and a/b < 1):
        while (a*d <= b*c):
            a = a + 1
            b = b + 1
            cd = math.gcd(a,b)
            a = a // cd
            b = b // cd
            n = n + 1
            if (a == c and b == d):
                return n

rs = solve(a,b,c,d)
if rs == None:
    print(0)
else:
    print(rs)
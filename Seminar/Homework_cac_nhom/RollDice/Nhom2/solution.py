k,n = list(map(int,input().split()))
count = 0
def Rolldice(n,k,sum=0,flag = True):
    global count
    if(k==0 and sum ==n):
        count += 1
    else:
        if((sum + k > n) or (sum + 6*k <n )):
            return
        for i in range(1,7):
            sum += i
            Rolldice(n,k-1,sum,False)
            sum -= i
Rolldice(n,k,0)
print(count)
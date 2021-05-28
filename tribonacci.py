def tribonacci(n):
    if(n==0 or n==1 or n==2):
        return 0
    elif(n==3):
        return 1
    else:
        return (tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3))
def printtrib(n):
    for i in range(1,n):
        print(tribonacci(i)," ",end="")
n=int(input())
printtrib(n)



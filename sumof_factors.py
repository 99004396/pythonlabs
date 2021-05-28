def sumOfFactors(n):
    s=0
    if(n<=0):
        print("No factors")
    elif(n==1):
        print("1")
    else:
        for i in range(1,n+1):
            if(n%i==0):
                s+=i
        print(s)
n=int(input())
sumOfFactors(n)
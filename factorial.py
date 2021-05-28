def factorial(n):
    f=1
    if(n<=0):
        print("Incorrect")
    elif(n==1):
        print("1")
    else:
        for i in range(1,n+1):
            f*=i;
        print(f)
n=int(input())
factorial(n)


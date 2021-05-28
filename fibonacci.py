def fibonacci(n):
    if(n==0):
        print("Incorrect input")
    if(n==1):
        print("0")
    n1=0
    n2=1
    c=0
    while c<n:
        print(n1)
        f=n1+n2
        n1=n2
        n2=f
        c+=1
n=int(input())
fibonacci(n)
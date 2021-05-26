def gcd(x,y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i==0):
            gcd=i
        i=i+1
    return gcd
x=int(input())
y=int(input())
print(gcd(x,y))
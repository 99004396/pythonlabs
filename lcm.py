def lcm(x,y):
    max=0
    if(x>y):
        max=x
    else:
        max=y
    while(True):
        if((max%x==0) and (max%y==0)):
            lcm=max
            break
        max=max+1
    return lcm
x=int(input())
y=int(input())
print(lcm(x,y))
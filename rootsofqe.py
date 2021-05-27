import math
def roots(a,b,c):
    d=(b*b)-4*a*c
    if(d>0):
        r1= -b + math.sqrt(d) / (2 * a)
        r2=-b - math.sqrt(d) / (2 * a)
        print("Root1 is : ",r1,"\nRoot2 is : ",r2)
    elif(d==0):
        r1=r2=-b/(2*a)
        print("Root1 is : ", r1, "\nRoot2 is : ", r2)
    else:
        r1=-b/(2*a)
        r2=math.sqrt(-d)/(2*a)
        print("Root1 is : ", r1, "\nRoot2 is : ", r2)
a=float(input())
b=float(input())
c=float(input())
roots(a,b,c)
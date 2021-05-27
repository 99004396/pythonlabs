def type(a,b,c):
    if(a==b and b==c and c==a):
        print("Equilateral triangle")
    elif((a*a+b*b==c*c) or (b*b+c*c==a*a) or (c*c+a*a==b*b)):
        print("Right angle triangle")
    elif(a==b or b==c or a==c):
        print("Isoceles triangle")
    elif(a!=b or b!=c or c!=a):
        print("Scalene triangle")
    else:
        print("Not of any type")
a=int(input())
b=int(input())
c=int(input())
type(a,b,c)


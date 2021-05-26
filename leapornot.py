def leap(n):
    if(n%400==0):
        print("Leap year")
    elif(n%100==0):
        print("Non leap")
    elif(n%4==0):
        print("Leap year")
    else:
        print("Non Leap")
n=int(input())
leap(n)
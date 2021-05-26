def rev(n):
    rev=0
    while n != 0:
        rem=n % 10
        rev=(rev*10)+rem
        n=n//10
    return rev
def sum(n):
    sum = 0
    while n != 0:
        rem = n % 10
        sum+=rem
        n=n//10
    return sum
n=int(input());
print("Reverse of a number is : ",rev(n))
print("Sum of digits : ",sum(n))

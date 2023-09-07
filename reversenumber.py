def reverse(n):
    sum=0
    for i in range(b):
        d=n%10
        sum=sum*10+d
        n=n//10
    return f"Reverse is {sum}"

a=int(input("Number: "))
b=len(str(a))
print(reverse(a))



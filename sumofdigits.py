def sum(n):
    sum=0
    while n>1:
        d=n%10
        sum=sum+d
        n=n//10
    print(sum)
a=int(input("number: "))
sum(a)
def armstrong(n1,n2):
    for i in range(n1,n2):
        l=len(str(i))
        num=i
        sum=0
        while i>0:
            d=i%10
            sum=sum+(d**l)
            i=i//10
            s=sum
        if (s==num):
            print(s)
n1=int(input("enter the first limit"))
n2=int(input("enter the second limit"))
armstrong(n1,n2)
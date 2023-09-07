c=[]
def oddeven(*num):
    a=[]
    b=[]
    for i in num:
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    return f"even : {a} \nodd  : {b}"
z = int(input("number of elements: "))
for i in range(z):
    l = int(input(f"Number {i+1} : "))
    c.append(l)
print(oddeven(*c))
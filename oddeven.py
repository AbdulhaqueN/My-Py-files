a = []
b = []
def oddeven():
    s=int(input("How many in each list? "))
    for i in range(s):
        x=int(input(f"Number{i+1}: "))
        a.append(x)
    print("-----List 2------")
    for i in range(s):
        y=int(input(f"Number{i+1}: "))
        b.append(y)
    for i in a:
        if i%2==0:
            b.append(i)
            a.remove(i)
    for i in b:
        if i%2!=0:
            a.append(i)
            b.remove(i)
    return f"Odd={a}   Even={b}"
print(oddeven())

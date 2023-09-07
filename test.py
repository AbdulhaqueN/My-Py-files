o=[1,2,3,4,5]
e=[6,7,8,9,10]

for i in o:
    if i%2==0:
        e.append(i)
        o.remove(i)
for i in e:
    if i%2!=0:
        o.append(i)
        e.remove(i)
print("Odd list: ",o)
print("Even list: ",e)

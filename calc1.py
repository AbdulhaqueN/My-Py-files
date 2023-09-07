from calc2 import *

a=int(input("How many numbers: "))
c=[]
for i in range(a):
    b=int(input(f"Number {i+1}: "))
    c.append(b)

op=input("Operation (+ - * /) : ")
if op=="+":
    print(sum(*c))
elif op=="-":
    print(diff(*c))
elif op=="/":
    print(division(*c))
elif op=="*":
    print(product(*c))
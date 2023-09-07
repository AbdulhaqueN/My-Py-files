def interest(p,r,t):
    i=(p*r*t)/100
    return i
def interest2():
    p = int(input("Principal Amount: "))
    r = int(input("Rate of interest: "))
    t = int(input("Time period in years: "))
    print("Simple Interest = ",interest(p,r,t))
interest2()

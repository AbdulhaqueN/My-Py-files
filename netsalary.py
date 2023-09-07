def salary():
    total=int(input("Whats ur total salary? "))
    deducted=int(input("How much is deducted from total salary? "))
    netsalary=total-deducted
    return f"Net salary= {netsalary}"
print(salary())
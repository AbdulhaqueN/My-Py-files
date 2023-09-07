def hello(name,age):
    print("hello ",name,"of age ",age)

hello("haque",23)

def product(x,y):
    c=x*y
    print(f"{x} x {y} = {c}")

def start():
    print("start")
def end():
    c=start()
    print(c,"now")
def sum(x,y):
    return x+y
end()

product(5,10)
print(sum(5,9))
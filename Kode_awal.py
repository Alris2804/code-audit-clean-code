def h(a, b):
    x = a * b
    if x > 100000:
        x = x - (x * 0.2)
    elif x > 50000:
        x = x - (x * 0.1)
    else:
        x = x - (x * 0.05)
    
    print("total:", x)
    
    if b == 1:
        print("member")
    else:
        print("non member")
    
    return x


data = [10000, 20000, 30000]

for i in data:
    h(i, 2)
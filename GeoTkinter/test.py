def g(*x, y=[]):
    print(x)
    for k in x:
        y.append(k)
        return y


L1 = g(3,2)
L1.append(4)
L2 = g(6)
print(L1)
print(L2)

from random import randint
x, y, n=[], [], int(input("n= "))
x.extend([randint(1, 200) for x in range(n)])
y.extend([randint(1, 200) for q in range(n)])
x1, y1=set(x), set(y)
print(x1, "\n", y1)
print(x1.union(y1), "\n",x1.intersection(y1))
print(x1.difference(y1))
print((x1.difference(y1)).union(y1.difference(x1)))
print((x1.difference(y1)).intersection(y1.difference(x1)))
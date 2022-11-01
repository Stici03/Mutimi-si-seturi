from random import randint
a, b, c, d, n=[], [], [], [], int(input("n= "))
a.extend([randint(0, 200) for x in range(n)])
b.extend([randint(0, 200) for x in range(n)])
c.extend([randint(0, 200) for x in range(n)])
d.extend([randint(0, 200) for x in range(n)])
A, X, Y, Z=set(a), set(b), set(c), set(d)
print(X,"\n",Y,"\n",Z)
if A.difference(X.union(Y).union(Z))==(A.difference(X)).intersection(A.difference(Y)).intersection(A.difference(Z)):
    print("Se verifica prima lege lui Morgan")
else:
    print("Nu se respecta prima lege lui Morgan")

if A.difference(X.intersection(Y).intersection(Z))==(A.difference(X)).union(A.difference(Y)).union(A.difference(Z)):
    print("Se respecta a 2 lege a lui Morgan")
else:
    print("Nu se respecta a doua lege a lui Morgan")
a, b={1, 3, "a", 4, "c", "d", 582}, {2, "a", "c", 8, 4, 9, "e", 3}
c=(a.union(b)).difference(a.intersection(b))
print(c)
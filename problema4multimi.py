from itertools import combinations
A={1, 2, 3, "A", "B", "C"}
for x in range(len(A)+1):
    comb=combinations(A, x)
    for i in list(comb):
        print(i, sep="\t")

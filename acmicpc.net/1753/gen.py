import random

V, E = 20000, 300000
K = 1
print(V, E)
print(K)
ns = list(range(1, 20001))
for i in range(E):
    print(*random.sample(ns, 2), random.randint(1, 10))

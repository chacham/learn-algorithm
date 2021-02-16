import random

# C = random.randint(1, 50)
C = 50
print(C)
for c in range(C):
    # N = random.randint(1, 100)
    # M = random.randint(1, 100)
    N = 100
    M = 100

    print(N, M)

    print(" ".join([str(random.randint(0, 50000)) for _ in range(N)]))
    print(" ".join([str(random.randint(0, 50000)) for _ in range(M)]))

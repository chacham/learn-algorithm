import random
print(100)
for i in range(100):
    print(300, 300)
    for i in range(300):
        print(" ".join([str(random.randint(0, 2000000)) for _ in range(300)]))
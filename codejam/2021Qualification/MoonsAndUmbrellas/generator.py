import random
print(100)
for i in range(100):
    print(random.randint(-100, 100), random.randint(-100, 100), ''.join([random.choice('CJ?') for _ in range(1000)]))
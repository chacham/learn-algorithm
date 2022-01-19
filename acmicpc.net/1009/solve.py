mod = [1, 1, 4, 4, 2, 1, 1, 4, 4, 2]

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        a, b = [int(x) for x in input().split()]
        print(((a ** (((b-1) % mod[a%10]) + 1)) % 10) or 10)

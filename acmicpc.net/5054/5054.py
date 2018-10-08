if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        n = int(input())
        x = [int(x) for x in input().split()]
        print((max(x) - min(x)) * 2)

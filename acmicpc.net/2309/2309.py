if __name__ == "__main__":
    H = [int(input()) for i in range(9)]
    total = sum(H)
    for i, j in [(i, j) for i in range(9) for j in range(i, 9) if i != j]:
        if total - H[i] - H[j] == 100:
            H.pop(i)
            H.pop(j - 1)
            break
    for i in sorted(H):
        print(i)

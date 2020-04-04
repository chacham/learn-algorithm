def INV(l):
    return [1 - b for b in l]

def REV(l):
    return list(reversed(l))

def solve_all(B):
    h = []
    t = []
    for i in range(5):
        print(len(h)+1)
        b = int(input())
        h.append(b)
    for i in range(B, B-5, -1):
        print(B-len(t))
        b = int(input())
        t.append(b)
    
    while len(h) + len(t) < B:
        # check if inverted
        for i in range(len(h)):
            if h[i] == t[i]:
                print(i+1)
                if int(input()) != h[i]:
                    h, t = INV(h), INV(t)
                break
        else:
            print(1)
            input()

        # check if reversed
        for i in range(len(h)):
            if h[i] != t[i]:
                print(i+1)
                if int(input()) != h[i]:
                    h, t = t, h
                break
        else:
            print(1)
            input()

        for i in range(4):
            print(len(h) + 1)
            b = int(input())
            h.append(b)

            print(B - len(t))
            b = int(input())
            t.append(b)

            if len(h) + len(t) >= B:
                break

    res = [str(int(b)) for b in h + REV(t)]
    print(''.join(res))
    RESULT = input()
    if RESULT == 'N':
        exit(1)


if __name__ == "__main__":
    T, B = map(int, input().split())

    for t in range(T):
        solve_all(B)

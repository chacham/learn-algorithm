import sys

if __name__ == "__main__":
    T, N, Q = map(int, input().split())
    for t in range(T):
        print(1, 2, 3)
        mid = int(input())
        res = [1, 2, 3]
        res.remove(mid)
        res.insert(1, mid)
        for n in range(4, N+1):
            L, R = 0, len(res)
            while L < R-2:
                ml, mr = L + (R-L)//3, L + (R-L)//3*2
                print(res[ml], res[mr], n)
                recv = int(input())
                if recv == res[ml]:
                    R = ml
                if recv == n:
                    L, R = ml+1, mr
                if recv == res[mr]:
                    L = mr+1
            if L > len(res)-2:
                L = len(res)-2
            print(res[L], res[L+1], n)
            recv = int(input())
            if recv == res[L]:
                res.insert(L, n)
            elif recv == n:
                res.insert(L+1, n)
            else: # recv == res[L+1]:
                res.insert(L+2, n)
        print(' '.join(map(str, res)))
        success = int(input())
        if not success:
            exit(0)

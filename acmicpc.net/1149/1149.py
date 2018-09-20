if __name__ == "__main__":
    N = int(input())

    Rcost = []
    Gcost = []
    Bcost = []
    for r, g, b in [map(int, input().split()) for i in range(N)]:
        Rcost.append(r)
        Gcost.append(g)
        Bcost.append(b)
    R = [Rcost[0]]
    G = [Gcost[0]]
    B = [Bcost[0]]

    for i in range(N-1):
        R.append(min(G[i], B[i]) + Rcost[i+1])
        G.append(min(R[i], B[i]) + Gcost[i+1])
        B.append(min(G[i], R[i]) + Bcost[i+1])
    
    print(min(R[-1], G[-1], B[-1]))

def solve(N, P):
    row, col = 0, 0
    lydia = []
    for p in P:
        lydia.append((row, col))
        if p == 'E':
            col += 1
        else:
            row += 1

    if lydia[1] == (0, 1) and lydia[-1] == (N-2, N-1):
        return 'S' * (N-1) + 'E' * (N-1)
    if lydia[1] == (1, 0) and lydia[-1] == (N-1, N-2):
        return 'E' * (N-1) + 'S' * (N-1)
    
    if lydia[1] == (1, 0): # Find horizontal bar
        for i in range(len(lydia) - 2):
            if lydia[i][0] == lydia[i+1][0] and lydia[i+1][0] == lydia[i+2][0]:
                row, col = lydia[i+1]
                break
        return 'E' * col + 'S' * (N-1) + 'E' * (N-1-col)
    else: # Find vertical bar
        for i in range(len(lydia) - 2):
            if lydia[i][1] == lydia[i+1][1] and lydia[i+1][1] == lydia[i+2][1]:
                row, col = lydia[i+1]
                break
        return 'S' * row + 'E' * (N-1) + 'S' * (N-1-row)

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        P = input()

        print('Case #{}: {}'.format(t+1, solve(N, P)))

            
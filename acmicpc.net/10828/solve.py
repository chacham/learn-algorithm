import sys
input=sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    stack = []
    for _ in range(N):
        op, *n = input().split()
        if op == 'push':
            stack.append(int(n[0]))
        elif op == 'pop':
            print(stack.pop()) if stack else print(-1)
        elif op == 'size':
            print(len(stack))
        elif op == 'empty':
            print(0) if stack else print(1)
        elif op == 'top':
            print(stack[-1]) if stack else print(-1)

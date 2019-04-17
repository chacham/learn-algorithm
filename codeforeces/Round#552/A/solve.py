if __name__ == "__main__":
    inputs = sorted([int(x) for x in input().split()])
    sumOfAll = inputs.pop()
    print(*[sumOfAll - x for x in inputs])

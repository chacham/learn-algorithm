def abbreviatable(S, sub):
    subIdx = 0
    for c in S:
        if subIdx >= len(sub):
            return True
        if c == sub[subIdx]:
            subIdx += 1
    return subIdx >= len(sub)

if __name__ == "__main__":
    S = input()
    if abbreviatable(S, "UCPC"):
        print("I love UCPC")
    else:
        print("I hate UCPC")

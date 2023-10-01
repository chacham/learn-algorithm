import sys
input = sys.stdin.readline

def isConsistent(phoneNumbers):
    trie = {}
    for phoneNumber in phoneNumbers:
        createdNewNode = False
        currentRoot = trie
        for c in phoneNumber:
            if 'END' in currentRoot:
                return False
            if c not in currentRoot:
                currentRoot[c] = {}
                createdNewNode = True
            currentRoot = currentRoot[c]
        else:
            currentRoot['END'] = True
        if not createdNewNode:
            return False
    return True

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        phoneNumbers = [input().strip() for _ in range(N)]
        if isConsistent(phoneNumbers):
            print("YES")
        else:
            print("NO")

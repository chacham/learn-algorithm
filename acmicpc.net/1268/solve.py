if __name__ == "__main__":
    N = int(input())
    GRADE_CLASSES = []
    for n in range(N):
        GRADE_CLASSES.append([int(g) for g in input().split()])
    
    maxFriends = -1
    banjang = -1
    for student in range(N):
        friends = set()
        for i in range(N):
            for j in range(5):
                if GRADE_CLASSES[student][j] == GRADE_CLASSES[i][j]:
                    friends.add(i)
        if maxFriends < len(friends):
            banjang = student + 1
            maxFriends = len(friends)

    print(banjang)

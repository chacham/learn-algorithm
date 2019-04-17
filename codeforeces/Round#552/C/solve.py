if __name__ == "__main__":
    foods = [int(x) for x in input().split()]
    eat = [0, 1, 2, 0, 2, 1, 0]

    fullWeeks = min(foods[0] // 3, foods[1] // 2, foods[2] // 2)
    foods[0] -= fullWeeks * 3
    foods[1] -= fullWeeks * 2
    foods[2] -= fullWeeks * 2

    restDays = 0
    for i in range(7):
        eattenRest = [0, 0, 0]
        now = i
        tmpRestDays = -1
        while foods[0] >= eattenRest[0] and foods[1] >= eattenRest[1] and foods[2] >= eattenRest[2]:
            eattenRest[eat[now]] += 1
            now = (now + 1) % 7
            tmpRestDays += 1
        restDays = max(tmpRestDays, restDays)
    print(fullWeeks * 7 + restDays)
    
def PRINT(A, B, ground):
    for i in range(B, 0, -1):
        print(ground[i][1:])

DIR = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3,
    0: 'N',
    1: 'E',
    2: 'S',
    3: 'W',
    }

def run(robots, ground, robot, command, repeat, A, B):
    if command == 'L':
        robots[robot][2] = DIR[(DIR[robots[robot][2]] - repeat) % 4]
        return False
    elif command == 'R':
        robots[robot][2] = DIR[(DIR[robots[robot][2]] + repeat) % 4]
        return False
    else: # "F"
        if robots[robot][2] == 'N':
            direction = (1, 0)
        elif robots[robot][2] == 'E':
            direction = (0, 1)
        elif robots[robot][2] == 'S':
            direction = (-1, 0)
        elif robots[robot][2] == 'W':
            direction = (0, -1)
        for i in range(repeat):
            pos = (robots[robot][0], robots[robot][1])
            nextPos = (pos[0] + direction[0], pos[1] + direction[1])
            if nextPos[0] <= 0 or nextPos[0] > B or nextPos[1] <= 0 or nextPos[1] > A:
                return [robot]
            if ground[nextPos[0]][nextPos[1]]:
                return [robot, ground[nextPos[0]][nextPos[1]]]
            ground[nextPos[0]][nextPos[1]] = robot            
            ground[pos[0]][pos[1]] = 0
            robots[robot][0] += direction[0]
            robots[robot][1] += direction[1]

if __name__ == "__main__":
    A, B = map(int, input().split())
    N, M = map(int, input().split())

    ground = [[0] * (A + 1) for i in range(B + 1)]
    
    robots = [0]
    for i in range(1, N+1):
        col, row, dir = input().split()
        col, row = int(col), int(row)
        ground[row][col] = i
        robots.append([row, col, dir])
    commands = []
    for i in range(M):
        robot, command, repeat = input().split()
        commands.append([int(robot), command, int(repeat)])
    
    # PRINT(A, B, ground)
    # print('r', robots)
    # print('r', commands)

    for robot, command, repeat in commands:
        result = run(robots, ground, robot, command, repeat, A, B)
        if result:
            if len(result) == 1:
                print("Robot", result[0], "crashes into the wall")
            else:
                print("Robot", result[0], "crashes into robot", result[1])
            break
        # print()
        # PRINT(A, B, ground)
        # print()
    else:
        print("OK")
    
    # print(robots)
    # print(commands)
    # PRINT(A, B, ground)
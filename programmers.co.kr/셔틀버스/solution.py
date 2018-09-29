def solution(n, t, m, timetable):
    buses = []
    for i in range(n):
        offset = i * t
        hh = 9 + (offset // 60)
        mm = offset % 60
        buses.append([hh, mm, m])

    passengers = []
    for time in timetable:
        hh, mm = map(int, time.split(":"))
        passengers.append((hh, mm))
    passengers.sort(key=lambda x: x[1])
    passengers.sort(key=lambda x: x[0])

    boarded = []
    busIndex = 0
    passengerIndex = 0
    while True:
        if busIndex >= n or passengerIndex >= len(passengers):
            break

        bus = buses[busIndex]
        passenger = passengers[passengerIndex]

        if bus[0] > passenger[0] or (bus[0] == passenger[0] and bus[1] >= passenger[1]):
            bus[2] -= 1
            boarded.append(passenger)
            passengerIndex += 1
            if bus[2] == 0:
                busIndex += 1
        else:
            busIndex += 1
    
    if buses[-1][2] > 0:
        return "{:02d}:{:02d}".format(buses[-1][0], buses[-1][1])
    else:
        hh, mm = boarded[-1]
        hh = hh - 1 if mm == 0 else hh
        mm = 59 if mm == 0 else mm - 1
        return "{:02d}:{:02d}".format(hh, mm)

if __name__ == "__main__":
    inputs = [
        (1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]),
        (2, 10, 2, ["09:10", "09:09", "08:00"]),
        (2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]),
        (1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]),
        (1, 1, 1, ["23:59"]),
        (10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]),
        (2, 1, 1, ["00:01", "00:01", "00:01"]),
        (2, 5, 2, ["09:05", "09:05", "09:05", "09:05"]),
        (2, 1, 2, ["09:00", "09:00", "08:59", "08:59", "09:01", "09:01"])
    ]
    for n, t, m, timetable in inputs:
        print(solution(n, t, m, timetable))

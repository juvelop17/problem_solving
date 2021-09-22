


car = {}
timeSum = {}
cost = {}

def timeNum(timeStr):
    hour, minute = timeStr.split(':')
    return int(hour) * 60 + int(minute)

def solution(fees, records):
    answer = []

    normalTime, normalPrice, timeLimit, priceLimit = fees

    for record in records:
        timeStr, carNum, inout = record.split()
        if inout == 'IN':
            car[carNum] = timeNum(timeStr)
            if carNum not in timeSum:
                timeSum[carNum] = 0
        else:
            duration = (timeNum(timeStr) - car[carNum])
            timeSum[carNum] += duration
            del car[carNum]
    # print(timeSum)

    for carNum, time in car.items():
        timeStr = '23:59'
        duration = (timeNum(timeStr) - time)
        timeSum[carNum] += duration
    # print(timeSum)

    for carNum, totalTime in timeSum.items():
        if totalTime <= normalTime:
            cost[int(carNum)] = normalPrice
        else:
            if (totalTime - normalTime) % timeLimit == 0:
                cost[int(carNum)] = normalPrice + ((totalTime - normalTime) // timeLimit) * priceLimit
            else:
                cost[int(carNum)] = normalPrice + ((totalTime - normalTime) // timeLimit + 1) * priceLimit
    # print(cost)

    sortList = []
    for s in sorted(cost):
        sortList.append(cost[s])
    # print(sortList)

    return sortList


if __name__ == '__main__':
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

    # fees = [120, 0, 60, 591]
    # records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

    print(solution(fees, records))

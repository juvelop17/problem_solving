def timeToInt(time):
    li = time.split(':')
    return int(li[0])*60*60 + int(li[1])*60 + int(li[2])

def intToTime(num):
    s = num % 60
    num //= 60
    m = num % 60
    num //= 60
    h = num
    return f"{h:02}:{m:02}:{s:02}"


def solution(play_time, adv_time, logs):
    play_int = timeToInt(play_time)
    adv_int = timeToInt(adv_time)

    subSum = [0 for _ in range(play_int+1)]
    for log in logs:
        li = log.split('-')
        subSum[timeToInt(li[0])] += 1
        subSum[timeToInt(li[1])] -= 1

    for i in range(1, play_int+1):
        subSum[i] += subSum[i-1]

    for i in range(2, play_int+1):
        subSum[i] += subSum[i-1]

    maxTime = 0
    curSum = subSum[min(play_int, adv_int)]
    maxSum = curSum

    for s in range(0, play_int):
        e = s + adv_int
        if e > play_int:
            break
        curSum = subSum[e] - subSum[s]
        if maxSum < curSum:
            maxSum = curSum
            maxTime = s + 1

    return intToTime(maxTime)


if __name__ == '__main__':
    play_time, adv_time, logs = "02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    # play_time, adv_time, logs = "99:59:59",	"25:00:00",	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
    # play_time, adv_time, logs = "50:00:00",	"50:00:00",	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

    print(solution(play_time, adv_time, logs))

    # print(intToTime(100))
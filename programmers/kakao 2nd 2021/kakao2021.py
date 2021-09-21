import requests
import json
import math
import heapq

token = '09ceb13d9d61375d8f403a0b48e0528e'
baseURL = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
MAX_TIME = 720

authKey = ''
problem = -1
time = -1
N = -1
totalDist = 0
totalFail = 0
bike = []
truck = []
truckCnt = -1

ret = []
req = []


def init(pnum):
    global authKey, time, truck, bike, req, ret, truckCnt

    problem = pnum
    if problem == 1:
        N = 5
        truckCnt = 5
    else:
        N = 60
        truckCnt = 10
    bike = [[0 for _ in range(N)] for _ in range(N)]
    truck = [{} for _ in range(truckCnt)]

    res = startAPI(problem)
    print(res)
    res.raise_for_status()
    resJson = res.json()
    authKey = resJson['auth_key']
    time = resJson['time']

    req = [[] for _ in range(MAX_TIME)]
    ret = [[] for _ in range(MAX_TIME)]


def startAPI(problem):
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}
    data = {'problem': problem}
    return requests.post(baseURL + '/start', headers=headers, data=json.dumps(data))


def locationsAPI():
    headers = {'Content-Type': 'application/json', 'Authorization': authKey}
    res = requests.get(baseURL + '/locations', headers=headers)
    res.raise_for_status()
    rjson = res.json()
    for loc in rjson['locations']:
        x = loc['id'] // N
        y = loc['id'] % N
        bike[x][y] = loc['located_bikes_count']


def trucksAPI():
    headers = {'Content-Type': 'application/json', 'Authorization': authKey}
    res = requests.get(baseURL + '/trucks', headers=headers)
    print(res)

    res.raise_for_status()
    rjson = res.json()
    for tr in rjson['trucks']:
        truck[tr['id']]['location_id'] = tr['location_id']
        truck[tr['id']]['loaded_bikes_count'] = tr['loaded_bikes_count']


def parseDocument(i):
    global req
    with open('./problem' + str(problem) + '_day-' + str(i) + '.json', 'r') as f:
        for k, v in json.load(f).items():
            for arr in v:
                req[int(k)].append(arr[:])


def findHotPlace():
    hotPlace = [[] for _ in range(3)]
    for i in range(1, 4):
        with open('./problem2_day-' + str(i) + '.json', 'r') as f:
            jsonLoad = json.load(f)
            jsonSort = sorted(list(zip(list(map(int, jsonLoad.keys())), jsonLoad.values())))
            # print(jsonSort)

            reqCnt = [0 for _ in range(N*N)]
            placeCnt = 0
            for k, v in jsonSort:
                for arr in v:
                    reqCnt[arr[0]] += 1

                if k > 0 and k % 240 == 0:
                    li = sorted([[i, reqCnt[i]] for i in range(len(reqCnt))], key=(lambda x: -x[1]))
                    print(li)
                    hotPlace[placeCnt].append(li[0][0])
                    placeCnt += 1
                    reqCnt = [0 for _ in range(N*N)]

            li = sorted([[i, reqCnt[i]] for i in range(len(reqCnt))], key=(lambda x: -x[1]))
            print(li)
            hotPlace[placeCnt].append(li[0][0])

    return hotPlace


def sendLocal(commands):
    global totalDist, totalFail

    status = 'ready'
    ntime = time + 1
    failCnt = 0
    for r in ret[time]:
        x = r // N
        y = r % N
        bike[x][y] += 1

    for r in req[time]:
        sx = r[0] // N
        sy = r[0] % N
        if bike[sx][sy] == 0 or time + r[2] >= MAX_TIME:
            failCnt += 1
            continue
        bike[sx][sy] -= 1
        ret[time + r[2]].append(r[1])
    totalFail += failCnt

    for command in commands:
        locid = truck[command["truck_id"]]['location_id']
        for comm in command["truck_id"]['command']:
            if comm == 1:
                locid += 1
                totalDist += 100
            elif comm == 2:
                locid += N
                totalDist += 100
            elif comm == 3:
                locid -= 1
                totalDist += 100
            elif comm == 4:
                locid -= N
                totalDist += 100
            elif comm == 5:
                if bike[locid // N][locid % N]:
                    truck[command["truck_id"]]['loaded_bikes_count'] += 1
                    bike[locid // N][locid % N] -= 1
            elif comm == 6:
                if truck[command["truck_id"]]['loaded_bikes_count']:
                    truck[command["truck_id"]]['loaded_bikes_count'] -= 1
                    bike[locid // N][locid % N] += 1

    if ntime == 720:
        status = 'finished'
    res = {'status': status, 'time': ntime, 'failed_requests_count': failCnt, 'distance': totalDist}
    return res


def simulateLocal(day):
    global problem, bike, truck

    locationsAPI()
    trucksAPI()
    parseDocument(day)

    while time < MAX_TIME:

        totalBike = 0
        for i in range(N):
            for j in range(N):
                totalBike += bike[i][j]
        avgBike = totalBike // (N*N)

        commands = []
        heap = []
        for i in range(N*N):
            for j in range(truckCnt):
                truckLoc = truck[j]['location_id']
                tx = truckLoc // N
                ty = truckLoc % N
                ix = i // N
                iy = i % N
                heapq.heappush(heap, [])




        res = sendLocal(commands)
        if res['status'] == 'ready':
            time = res['time']
            print(res['failed_requests_count'], res['distance'])




def simulateServer(prob):
    pass


def score():
    headers = {'Content-Type': 'application/json', 'Authorization': authKey}
    return requests.get(baseURL + '/score', headers=headers)


if __name__ == '__main__':
    scores = []

    init(1)
    simulateLocal(3)
    scores.append(score().json()['score'])

    print(scores)

    print(findHotPlace())

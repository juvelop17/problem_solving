import requests
import json

token = 'b5ced343d3d8e174c84075b2326ccb36'
baseURL = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
MAX_TIME = 720
MAX_TRUCK_BIKE = 20
alpha = 0.1 # 거리와 개수에대한 가중치

authKey = ''
problem = -1
time = -1
N = -1
bike = []
truck = []
truckCnt = -1


def init(pnum):
    global N, problem, authKey, time, bike, truck, truckCnt

    problem = pnum
    if problem == 1:
        N = 5
        truckCnt = 5
    else:
        N = 60
        truckCnt = 10
    bike = [0 for _ in range(N*N)]
    truck = [{} for _ in range(truckCnt)]

    res = startAPI(problem)
    resJson = res.json()
    authKey = resJson['auth_key']
    time = resJson['time']


def startAPI(problem):
    """
    API 시작
    :param problem: 문제 번호
    :return:
    """
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}
    data = {'problem': problem}
    return requests.post(baseURL + '/start', headers=headers, json=data)

def locationsAPI():
    headers = {'Content-Type': 'application/json', 'Authorization': authKey}
    res = requests.get(baseURL + '/locations', headers=headers)
    rjson = res.json()
    for loc in rjson['locations']:
        bike[loc['id']] = loc['located_bikes_count']

def trucksAPI():
    headers = {'Content-Type': 'application/json', 'Authorization': authKey}
    res = requests.get(baseURL + '/trucks', headers=headers)
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

def loadBike(avgBike, tid, commList):
    locid = truck[tid]['location_id']
    while len(commList[tid]) < 10 and truck[tid]['loaded_bikes_count'] < MAX_TRUCK_BIKE and bike[locid] > avgBike:
        truck[tid]['loaded_bikes_count'] += 1
        bike[locid] -= 1
        commList[tid].append(5)

def unloadBike(avgBike, tid, commList):
    locid = truck[tid]['location_id']
    while len(commList[tid]) < 10 and truck[tid]['loaded_bikes_count'] > 0:
        truck[tid]['loaded_bikes_count'] -= 1
        bike[locid] += 1
        commList[tid].append(6)

def move(tid, destid, commList):
    locid = truck[tid]['location_id']

    # 가로 이동
    truck[tid]['location_id'] += N * (destid // N - locid // N)
    if destid // N > locid // N:
        commList[tid].extend([2] * abs(destid // N - locid // N))
    elif destid // N < locid // N:
        commList[tid].extend([4] * abs(destid // N - locid // N))

    # 세로 이동
    truck[tid]['location_id'] += destid % N - locid % N
    if destid % N > locid % N:
        commList[tid].extend([1] * abs(destid % N - locid % N))
    elif destid % N < locid % N:
        commList[tid].extend([3] * abs(destid % N - locid % N))

def send(data):
    headers = {'Content-Type': 'application/json', 'Authorization': authKey}
    res = requests.put(baseURL + '/simulate', headers=headers, json=data)
    return res


def simulate():
    global time

    while time < MAX_TIME:
        # 위치 정보 업데이트
        locationsAPI()
        trucksAPI()
        avgBike = sum(bike) // len(bike)

        # bike 정렬
        maxBikeSort = sorted(list(zip(range(N*N), bike)), key=lambda x:(-x[1], x[0]))
        # print('maxBikeSort', maxBikeSort[:10])

        # 목적지 설정
        work = [-1 for _ in range(truckCnt)]
        for locid, bikeCnt in maxBikeSort[:truckCnt]:
            minDist = 100000
            minTid = -1
            for tid in range(truckCnt):
                if work[tid] != -1:
                    continue
                tloc = truck[tid]['location_id']
                tx = tloc // N
                ty = tloc % N
                bx = locid // N
                by = locid % N
                if minDist > abs(tx-bx) + abs(ty-by):
                    minDist = abs(tx-bx) + abs(ty-by)
                    minTid = tid
            work[minTid] = locid

        commList = [[] for _ in range(truckCnt)]
        # 명령 생성
        for tid in range(truckCnt):
            if truck[tid]['loaded_bikes_count'] < avgBike:
                # max 이동
                destid = work[tid]
                move(tid, destid, commList)

                # 자전거 싣기
                loadBike(avgBike, tid, commList)

        # min bike 정렬
        minBikeSort = sorted(list(zip(range(N * N), bike)), key=lambda x: (x[1], x[0]))
        # print('minBikeSort', minBikeSort[:10])

        # 목적지 설정
        work = [-1 for _ in range(truckCnt)]
        for locid, bikeCnt in minBikeSort[:truckCnt]:
            minDist = 100000
            minTid = -1
            for tid in range(truckCnt):
                if work[tid] != -1:
                    continue
                tloc = truck[tid]['location_id']
                tx = tloc // N
                ty = tloc % N
                bx = locid // N
                by = locid % N
                if minDist > abs(tx - bx) + abs(ty - by):
                    minDist = abs(tx - bx) + abs(ty - by)
                    minTid = tid
            work[minTid] = locid

        # 명령 생성
        for tid in range(truckCnt):
            # min 이동
            destid = work[tid]
            move(tid, destid, commList)

            # 자전거 내리기
            unloadBike(avgBike, tid, commList)

        data = {}
        data['commands'] = []
        for tid in range(truckCnt):
            comm = {'truck_id': tid, 'command': commList[tid][:10]}
            data['commands'].append(comm)

        # print(data)
        # print(truck)

        res = send(data)
        resJson = res.json()
        if resJson['status'] == 'ready':
            time = resJson['time']
            print(resJson['time'], resJson['failed_requests_count'], resJson['distance'])
        else:
            print(score().json()['score'])
            break


def score():
    headers = {'Content-Type': 'application/json', 'Authorization': authKey}
    return requests.get(baseURL + '/score', headers=headers)


if __name__ == '__main__':
    init(1)
    simulate()

    init(2)
    simulate()
    # print(findHotPlace())





import requests

baseURL = 'http://localhost:8000'
token = ''

authKey = ''


MAX_ELEVATOR = 4
MAX_PASSENGER = 8
HEIGHT = [5, 25, 25]

def startAPI(problem_id):
    sid = 'start'
    user_key = 'tester'
    number_of_elevators = MAX_ELEVATOR

    res = requests.post(f'{baseURL}/{sid}/{user_key}/{problem_id}/{number_of_elevators}')
    res.raise_for_status()
    resJson = res.json()
    return resJson

def oncallAPI(token):
    sid = 'oncalls'
    headers = {'X-Auth-Token': token}
    res = requests.get(f'{baseURL}/{sid}', headers=headers)
    res.raise_for_status()
    resJson = res.json()
    return resJson

def actionAPI(token, commands):
    sid = 'action'
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}
    data = {'commands': commands}
    res = requests.post(f'{baseURL}/{sid}', headers=headers, json=data)
    res.raise_for_status()
    resJson = res.json()
    return resJson


class Elevator:
    def __init__(self, eid, floor, passengers, status):
        self.eid = eid
        self.floor = floor
        self.pid = []
        for passenger in passengers:
            self.pid.append(passenger['id'])
        self.curStatus = status
        self.prevStatus = "STOP"
        self.dir = 0  # -1: 하강 0: 정지 1: 상승

    def setElevator(self, floor, passengers, status):
        self.floor = floor
        self.pid = []
        for passenger in passengers:
            self.pid.append(passenger['id'])
        self.prevStatus = self.curStatus
        self.curStatus = status

    def commIn(self):
        if self.curStatus == 'UPWARD' or self.curStatus == 'DOWNWARD':
            return 'STOP'
        elif self.curStatus == 'STOPPED':
            return 'OPEN'
        elif self.curStatus == 'OPENED':
            return 'ENTER'
        else:
            raise Exception('Undefined status commIn')

    def commOut(self):
        if self.curStatus == 'UPWARD' or self.curStatus == 'DOWNWARD':
            return 'STOP'
        elif self.curStatus == 'STOPPED':
            return 'OPEN'
        elif self.curStatus == 'OPENED':
            return 'EXIT'
        else:
            raise Exception('Undefined status commIn')

    def commMove(self, height):
        if self.floor == height:  # 반대방향으로 움직이기
            self.dir = -1
            if self.curStatus == 'UPWARD':
                return 'STOP'
            elif self.curStatus == 'OPENED':
                return 'CLOSE'
            return 'DOWN'
        elif self.floor == 1:  # 반대방향으로 움직이기
            self.dir = 1
            if self.curStatus == 'DOWNWARD':
                return 'STOP'
            elif self.curStatus == 'OPENED':
                return 'CLOSE'
            return 'UP'
        else:  # 움직이는 방향으로 움직이기
            if self.curStatus == 'OPENED':
                return 'CLOSE'

            if self.dir < 0:
                return 'DOWN'
            elif self.dir > 0:
                return 'UP'
            else: # 정지상태
                return 'UP'

class Call:
    def __init__(self, cid, timestamp, start, end):
        self.cid = cid
        self.timestamp = timestamp
        self.start = start
        self.end = end






def solution(problem, height):
    elevDict = {}
    callDict = {}

    res = startAPI(problem)
    token = res['token']
    timestamp = res['timestamp']
    for elevator in res['elevators']:
        elevDict[elevator['id']] = Elevator(elevator['id'], elevator['floor'], elevator['passengers'], elevator['status'])

    while True:
        print('token',token)
        building = [[] for _ in range(height + 1)]

        res = oncallAPI(token)
        timestamp = res['timestamp']
        print('calls', timestamp, res['calls'])
        print('elevators', timestamp, res['elevators'])

        for call in res['calls']:
            curCall = Call(call['id'], call['timestamp'], call['start'], call['end'])
            callDict[call['id']] = curCall
            building[curCall.start].append(curCall.cid)
        for elevator in res['elevators']:
            elevDict[elevator['id']].setElevator(elevator['floor'], elevator['passengers'], elevator['status'])

        if res['is_end']:
            break

        commList = []
        for eid in range(MAX_ELEVATOR):
            curElev = elevDict[eid]

            outList = []
            for cid in curElev.pid[:]:
                if callDict[cid].end == curElev.floor:
                    outList.append(cid)
                    curElev.pid.remove(cid)
            inList = []
            for cid in building[curElev.floor][:]:
                if len(curElev.pid) < MAX_PASSENGER:
                    inList.append(cid)
                    curElev.pid.append(cid)
                    building[curElev.floor].remove(cid)

            if len(outList): # 내리기
                commList.append({'elevator_id': eid, 'command': curElev.commOut(), 'call_ids': outList})
            elif len(inList): # 태우기
                commList.append({'elevator_id': eid, 'command': curElev.commIn(), 'call_ids': inList})
            else: # 움직이기
                commList.append({'elevator_id': eid, 'command': curElev.commMove(height)})

        print(commList)
        res = actionAPI(token, commList)


if __name__ == '__main__':
    problem = 2
    solution(problem, HEIGHT[problem])

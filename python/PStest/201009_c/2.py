
from queue import PriorityQueue
import datetime

def solution(n, customers):
    que = PriorityQueue()
    cnt_kiosk = [0 for _ in range(n)]

    for i in range(n):
        to_date = datetime.datetime.strptime('01/01 00:00:00', "%m/%d %H:%M:%S")
        que.put((to_date,i))

    idx = 0
    while idx < len(customers):
        node = que.get()
        print('node',node)
        customer = customers[idx]
        print('customer',customer)
        li = customer.split()
        to_date = datetime.datetime.strptime(li[0] + ' ' + li[1], "%m/%d %H:%M:%S")

        if node[0] >= to_date:
            que.put((node[0]+datetime.timedelta(minutes=int(li[2])), node[1]))
        else:
            new_date = to_date + datetime.timedelta(minutes=int(li[2]))
            que.put((new_date, node[1]))
        cnt_kiosk[node[1]] += 1
        print('cnt_kiosk',cnt_kiosk)
        idx += 1

    return max(cnt_kiosk)


# 도착날짜 도착시간 소요시간
n = 3
customers = ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]

# n = 2
# customers = ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]


print(solution(n, customers))














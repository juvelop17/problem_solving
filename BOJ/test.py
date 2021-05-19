from queue import PriorityQueue


que = PriorityQueue()

l = [4,2,2,1,2,1,8,2]
for n in l:
    que.put(n)

while not que.empty():
    print(que.get())

print('-------------------------')

for n in l:
    que.put(-n)

while not que.empty():
    print(-que.get())

print('-------------------------')

l = [(1, 'z'), (1, 'asdf'), (1, 'fjeo')]
for n in l:
    que.put(n)

while not que.empty():
    print(que.get())


print('-------------------------')

l = [[11, 'z'], [2, 'asdf'], [3, 'fjeo']]
for n in l:
    que.put(n)

while not que.empty():
    print(que.get())

print('-------------------------')

l = [['z', 1], ['asdf', 2], ['fjeo', 3]]
for n in l:
    que.put(n)

while not que.empty():
    print(que.get())






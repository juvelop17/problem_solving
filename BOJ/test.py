from queue import PriorityQueue


que = PriorityQueue()

que.put(1)
que.put(5)
que.put(4)
que.put(3)
que.put(2)
que.put(10)


while not que.empty():
    print(que.get())

class Node:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        if self.a == other.a:
            return self.b < other.b
        return self.a > other.a

    def __repr__(self):
        return f'({self.a} {self.b})'

que = PriorityQueue()
que.put(Node(1,2))
que.put(Node(10,1))
que.put(Node(2,5))
que.put(Node(1,5))
que.put(Node(10,5))
que.put(Node(1,29))
que.put(Node(2,1))

while not que.empty():
    print(que.get())


li = [1,2,3,4,5]

for l in li:
    print(l)
    li.remove(l)
    print(li)

print('----------')
li = [1,2,3,4,5]

for i in range(len(li)):
    print(li[i])
    li.remove(li[i])
    print(li)



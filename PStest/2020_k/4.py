import time

prev_time = time.time_ns()

class Node:
    def __init__(self, key):
        self.key = key
        self.cnt = 0
        self.child = {}
        self.isTerminated = False

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, s):
        curr_node = self.head

        for c in s:
            if c not in curr_node.child:
                curr_node.child[c] = Node(c)
            curr_node.cnt += 1
            curr_node = curr_node.child[c]
        curr_node.isTerminated = True

    def count(self, query):
        cnt = 0
        cur_node = self.head
        for i in range(len(query)):
            if query[i] == '?':
                cnt = cur_node.cnt
                return cnt
            if query[i] in cur_node.child:
                cur_node = cur_node.child[query[i]]
            else:
                return 0
        return -1

def solution(words, queries):
    answer = []

    t = [Trie() for _ in range(10001)]
    rt = [Trie() for _ in range(10001)]
    for w in words:
        t[len(w)].insert(w)
        rt[len(w)].insert(w[::-1])
    for query in queries:
        cnt = 0
        if query[0] != '?':
            q = query
            cnt = t[len(q)].count(q)
        else:
            q = query[::-1]
            cnt = rt[len(q)].count(q)
        answer.append(cnt)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao", "a"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
queries = ["frodo?"]

print(solution(words,queries))

print('time', time.time_ns()-prev_time)

# test_str = 'frodo'
# print(test_str,t.find(test_str))
# test_str = 'f'
# print(test_str,t.find(test_str))
# test_str = 'front'
# print(test_str,t.find(test_str))
# test_str = '?ront'
# print(test_str,t.find(test_str))
# test_str = 'frod?'
# print(test_str,t.find(test_str))
# test_str = 'froe?'
# print(test_str,t.find(test_str))









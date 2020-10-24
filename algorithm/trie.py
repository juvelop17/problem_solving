
class Node:
    def __init__(self, key):
        self.key = key
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
            curr_node = curr_node.child[c]
        curr_node.isTerminated = True

    def find(self, s):
        curr_node = self.head
        for c in s:
            if c in curr_node.child:
                curr_node = curr_node.child[c]
            else:
                return False
        if curr_node.isTerminated:
            return True
        return False

t = Trie()
t.insert('hi')
print(t.find('h'))
print(t.find('hi'))
print(t.find('hid'))
print(t.find('hj'))
print(t.find('a'))






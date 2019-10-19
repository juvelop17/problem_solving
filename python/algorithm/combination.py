

def combination(start):
    if len(pick) == n:
        res.append(pick[:])
        return

    for i in range(start,9):
        if memory[i] == 0:
            pick.append(li[i])
            memory[i] = 1
            combination(i+1)
            memory[i] = 0
            pick.pop()

li = [i for i in range(9)]
n = 2

res = []
pick = []
memory = [0 for _ in range(9)]
combination(0)
print(res)



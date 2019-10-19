def permutation():
    if len(pick) == 2:
        res.append(pick[:])
        return

    for i in range(len(li)):
        if memory[i] == 0:
            pick.append(li[i])
            memory[i] = 1
            permutation()
            memory[i] = 0
            pick.pop()

li = [i for i in range(9)]
n = 2

res = []
pick = []
memory = [0 for _ in range(9)]
permutation()
print(res)



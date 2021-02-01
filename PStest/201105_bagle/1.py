import time

ptime = time.time_ns()

# import sys
# sys.stdin = open('input.txt','r')


#####################################################

N = 4
ladder = [[1,0,1],[0,1,0],[0,0,1],[0,0,0],[1,0,0]]

def printMap(mp):
    for i in range(len(mp)):
        print('|',end='')
        for j in range(len(mp[0])):
            print(str(mp[i][j]).center(3),end='|')
        print()
    print()



def solution(n, ladder):
    answer = []

    # printMap(ladder)

    for i in range(n):
        ccol = i
        crow = 0
        while crow < len(ladder):
            if ccol - 1 >= 0 and ladder[crow][ccol - 1] == 1:
                ccol -= 1
            elif ccol + 1 < n and ladder[crow][ccol] == 1:
                ccol += 1
            crow += 1
        # print('ccol',ccol)
        answer.append(ccol + 1)

    return answer


print(solution(N, ladder))


#####################################################

print('time',time.time_ns()-ptime)


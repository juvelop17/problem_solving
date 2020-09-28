
import sys
sys.stdin = open('input.txt','r')
read = sys.stdin.readline


def solution(n,m,tiles):
    if m % 2 != 0:
        return False
    for tile in tiles:
        if tile[0][1] == tile[1][0]:
            return True

    return False

t = int(read())

for _ in range(t):
    n, m = list(map(int,read().split()))
    tiles = []
    for _ in range(n):
        tile = []
        tile.append(list(map(int,read().split())))
        tile.append(list(map(int,read().split())))
        tiles.append(tile)
    print('Yes' if solution(n,m,tiles) else 'No')










